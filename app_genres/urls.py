from django.conf.urls import url, include
# from .api.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    url(r'^api/', include('app_genres.api.urls'), name='apis'),
]
