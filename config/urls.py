from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from .urls_api import apiurls


# Generic URLs
urlpatterns = apiurls + [
    # API urls
    url(r"^tools/", include("app_tools.urls"), name="tools"),
    url(r"^movies/", include("app_movies.urls"), name="movies"),
    url(r"^cart/", include("app_cart.urls"), name="cart"),
    url(r"^auth/", include("app_auth.urls"), name="auth"),
    url(r"^admin/", admin.site.urls),
    # url(r"^$", listing, name='listing'),
    url(r"^", include("app_genres.urls"), name="genres"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
