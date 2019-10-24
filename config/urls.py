from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.urls import path


urlpatterns = [
    url(r'^/?$', include('app_home.urls'), name='home'),
    url(r'^genres/', include('app_genres.urls'), name='genres'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
