from django.conf.urls import url
from .views import login, register, logout, forgot, change


urlpatterns = [
    url(r"login$", login, name='auth-login'),
    url(r"register$", register, name='auth-register'),
    url(r"forgot$", forgot, name='auth-forgot'),
    url(r"change/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$", change, name='auth-change'),
    url(r"logout$", logout, name='auth-logout'),
]
