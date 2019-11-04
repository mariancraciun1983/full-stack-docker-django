from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                attrs['user'] = user
            else:
                raise serializers.ValidationError("Please enter a correct email and password")
        return attrs

class ForgotSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email__iexact=email).exists():
            user = User.objects.get(email__iexact=email)
            attrs['user'] = user
        else:
            raise serializers.ValidationError("Email not found")
        return attrs

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if email and User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return email

class ChangeSerializer(serializers.Serializer):
    uidb64 = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True)

    def validate_uidb64(self, uidb64):
        try:
            uidb64 = urlsafe_base64_decode(uidb64)
            self.current_user = User.objects.get(pk=uidb64)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("Failed to decode the uid code")
        return uidb64

    def validate(self, attrs):
        user = self.current_user
        token = attrs.get("token")
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError("Bad token")

        password = attrs.get("password")
        password_confirmation = attrs.get("password_confirmation")
        if password != password_confirmation:
            raise serializers.ValidationError("The two passswords must be the same")

        attrs['user'] = user
        return attrs
