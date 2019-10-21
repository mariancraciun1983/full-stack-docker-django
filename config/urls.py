from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', include('home.urls'), name='home'),
    url(r'^tools/', include('tools.urls')),
    url(r'^admin/', admin.site.urls),
]
