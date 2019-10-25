from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as django_auth_login
from django.contrib.auth import logout as django_auth_logout
from .forms import RegisterForm, LoginForm

def login(request):
    # if not request.user.is_anonymous:
    #     return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            django_auth_login(request, user)
            return redirect('home')
    else:
        form = LoginForm(initial={
            'email': 'john@example.com',
            'password': 'password',
        })

    return render(request, "auth/login.html", {
        "form": form
    })

@transaction.atomic
def register(request):
    if not request.user.is_anonymous:
        return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            
            # send welcome email:
            # user.atlas_email('client_email_welcome')

            # send signal
            # user_registered.send(sender=User, user=user, request=request)

            # log in user
            # user.backend = 'accounts.authentication.EmailOrUsernameModelBackend'
            
            django_auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm(initial={
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password',
        })

    return render(request, "auth/register.html", {
        "form": form
    })

def logout(request):
    django_auth_logout(request)
    return render(request, "auth/logout.html")
