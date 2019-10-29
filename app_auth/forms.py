from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()  # widget=forms.PasswordInput

    error_messages = {
        "invalid_login": "Please enter a correct email and password.",
        "inactive": "This account is inactive.",
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"], code="invalid_login"
                )

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class ForgotPasswordForm(forms.Form):
    email = forms.CharField()
    error_messages = {"invalid_email": "Email not found"}

    def __init__(self, *args, **kwargs):
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean_email(self):
        # check email uniqueness
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email__iexact=email).exists():
            self.user_cache = User.objects.get(email__iexact=email)
        else:
            raise forms.ValidationError(
                self.error_messages["invalid_email"], code="invalid_email"
            )
        return email

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class ChangePasswordForm(forms.Form):
    password = forms.CharField(required=True)  # widget=forms.PasswordInput
    password_confirmation = forms.CharField(required=True)  # widget=forms.PasswordInput
    error_messages = {"not_same_password": "Passwords are not the same"}

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        # check email uniqueness
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise forms.ValidationError(
                self.error_messages["not_same_password"], code="not_same_password"
            )
        return self.cleaned_data


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(
        error_messages={"duplicate_email": "A user with that email already exists."}
    )
    password = forms.CharField(min_length=4)  # widget=forms.PasswordInput

    def clean_email(self):
        # check email uniqueness
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email__iexact=email).exists():
            self.add_error(
                "email", self.fields["email"].error_messages["duplicate_email"]
            )
        return email

    def save(self, request):
        name = self.cleaned_data.get("name")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email").lower()

        # create user
        new_user = User.objects.create_user(
            email, email=email, password=password, first_name=name
        )
        new_user.is_active = True
        new_user.save()

        return new_user
