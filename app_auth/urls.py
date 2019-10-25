from django.conf.urls import url
from .views import login, register, logout


urlpatterns = [
    url(r"auth-login$", login, name='auth-login'),
    url(r"auth-register$", register, name='auth-register'),
    url(r"auth-logout$", logout, name='auth-logout'),
]
