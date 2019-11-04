from django.contrib.auth import login as django_auth_login
from django.contrib.auth import logout as django_auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction
from django.http import Http404
from django.middleware.csrf import rotate_token
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from app_user.tasks import send_email
from .forms import ChangePasswordForm, ForgotPasswordForm, LoginForm, RegisterForm


@csrf_protect
def login(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            django_auth_login(request, user)
            return redirect("home")
    else:
        form = LoginForm(initial={"email": "john@example.com", "password": "password"})

    return render(request, "auth/login.html", {"form": form})


@transaction.atomic
@csrf_protect
def register(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            send_email(user, "auth_welcome")
            django_auth_login(request, user)
            return redirect("home")
    else:
        form = RegisterForm(
            initial={
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password",
            }
        )

    return render(request, "auth/register.html", {"form": form})


@csrf_protect
def forgot(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = form.get_user()
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
            # this will prevent the user from refreshing/re-posting the page
            rotate_token(request)
            return render(request, "auth/forgot_sent.html", {"form": form})
    else:
        form = ForgotPasswordForm(initial={"email": "john@example.com"})

    return render(request, "auth/forgot.html", {"form": form})


@transaction.atomic
@csrf_protect
def change(request, uidb64, token):
    if not request.user.is_anonymous:
        return redirect("/")

    try:
        print(uidb64)
        print(token)
        uidb64 = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uidb64)
        if not default_token_generator.check_token(user, token):
            raise Http404
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        raise Http404

    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            messages.add_message(
                request,
                messages.INFO,
                "Your password was updated. You may now login with your new password!",
            )
            return redirect(reverse("auth-login"))
    else:
        form = ChangePasswordForm(
            initial={"password": "password", "password_confirmation": "password"}
        )
    return render(request, "auth/change.html", {"form": form})


def logout(request):
    django_auth_logout(request)
    return render(request, "auth/logout.html")
