from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    email = forms.CharField()
    password = forms.CharField() #widget=forms.PasswordInput 

    error_messages = {
        'invalid_login': "Please enter a correct email and password.",
        'inactive': "This account is inactive.",
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegisterForm(forms.Form):

    name = forms.CharField(max_length=255)
    email = forms.EmailField(error_messages={'duplicate_email': "A user with that email already exists."})
    password = forms.CharField(min_length=4)  #widget=forms.PasswordInput

    def clean_email(self):
        # check email uniqueness
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', self.fields['email'].error_messages['duplicate_email'])
        return email

    def save(self, request):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email').lower()

        # create user
        new_user = User.objects.create_user(email, email=email, password=password, first_name=name)
        new_user.is_active = True
        new_user.save()

        return new_user
