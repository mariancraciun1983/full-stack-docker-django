from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    # url(r'tools/', include('app_tools.urls'), name='tools'),
    url(r'^admin/', admin.site.urls),
    # url('', include('app_home.urls'), name='home'),
]
