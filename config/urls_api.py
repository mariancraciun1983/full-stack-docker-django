from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import viewsets
from rest_framework.response import Response


# A list of Apps (withouth the app_ prefix) that contain APIs
apps = ["genres", "movies", "cart", "auth"]

class IndexViewSet(viewsets.ViewSet):
    """ Provides a list of APP_NAME => APP_NAME_APIs urls pairs """
    def list(self, request):
        return Response(
            {app: request.build_absolute_uri("/api/" + app) for app in apps}
        )


router = routers.SimpleRouter()
router.register("api", IndexViewSet, basename="api-index")

apiurls = [url(r"^api-auth/", include("rest_framework.urls"))]
for app in apps:
    # ^api/APP_NAME/
    regex = r"^api/" + app + "/"
    # app_APP_NAME.api.urls
    urls = "app_%s.api.urls" % (app,)
    # api-APP_NAME
    name = "api-%s" % (app,)
    apiurls.append(
        url(regex, include(urls), name=name)
    )

apiurls.extend(router.urls)
