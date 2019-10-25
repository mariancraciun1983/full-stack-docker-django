from django.conf.urls import url
from .views import listing


urlpatterns = [
    url(r"^$", listing, name='home'),
    url(r"^genre/(?P<slug>\w+)$", listing, name='genres-genre'),
]
