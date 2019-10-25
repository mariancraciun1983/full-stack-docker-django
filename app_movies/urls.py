from django.conf.urls import url
from .views import details


urlpatterns = [
    url(r"^(?P<id>[a-z0-9-]+)/(?P<slug>\w+)", details, name='movies-movie'),
]
