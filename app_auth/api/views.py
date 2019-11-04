from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, ForgotSerializer, ChangeSerializer
from base.api.mixins import AtomicMixin
from base.api.token import token_for_user
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from app_user.tasks import send_email


class LoginView(viewsets.GenericViewSet):
    """Login a user."""

    http_method_names = ["head", "options", "post"]
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def get_user(self):
        return self.serializer.validated_data["user"]

    def create(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)
        user = self.get_user()
        token = token_for_user(user)
        return Response({"user_id": user.id, "token": token})


class RegisterView(AtomicMixin, viewsets.GenericViewSet):
    """Register a new user."""

    http_method_names = ["head", "options", "post"]
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create_user(self):
        email = self.serializer.validated_data["email"]
        name = self.serializer.validated_data["name"]
        password = self.serializer.validated_data["password"]

        # create user
        new_user = User.objects.create_user(
            email, email=email, password=password, first_name=name
        )
        new_user.save()
        return new_user

    def create(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)
        user = self.create_user()
        token = token_for_user(user)
        return Response({"user_id": user.id, "token": token})


class ForgotView(viewsets.GenericViewSet):
    """Initiate the password reset for a user."""

    http_method_names = ["head", "options", "post"]
    permission_classes = (AllowAny,)
    serializer_class = ForgotSerializer

    def get_user(self):
        return self.serializer.validated_data["user"]

    def create(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)
        user = self.get_user()
        email_context = {
            "reset_url": "http://%s%s"
            % (
                request.META["HTTP_HOST"],
                reverse(
                    "auth-change",
                    kwargs={
                        "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                    },
                ),
            )
        }
        send_email(user, "auth_forgot", email_context)
        return Response({
            "sent": True
        })


class ChangeView(AtomicMixin, viewsets.GenericViewSet):
    """Change the password using a token"""

    http_method_names = ["head", "options", "post"]
    permission_classes = (AllowAny,)
    serializer_class = ChangeSerializer

    def get_user(self):
        return self.serializer.validated_data["user"]

    def get_password(self):
        return self.serializer.validated_data["password"]

    def create(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)
        user = self.get_user()
        password = self.get_password()
        user.set_password(password)
        user.save()
        return Response({
            "changed": True
        })
