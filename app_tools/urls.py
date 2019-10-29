from django.conf.urls import url
from .views import switch_design


urlpatterns = [
    url(r"^switch-theme/(?P<design>light|dark)", switch_design, name='tools-switch-theme'),
]
