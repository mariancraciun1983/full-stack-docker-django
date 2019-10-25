from django.shortcuts import render


def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/register.html")

def logout(request):
    return render(request, "auth/logout.html")
