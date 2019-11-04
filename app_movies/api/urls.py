from rest_framework import routers
from .views import ListViewSet

routeList = (
    ('', ListViewSet),
)

router = routers.DefaultRouter()
for route in routeList:
    router.register(route[0], route[1], basename='movies-'+route[0])

urlpatterns = router.urls
