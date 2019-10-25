from rest_framework import routers
from .views import ListViewSet

routeList = (
    ('list', ListViewSet),
)

router = routers.DefaultRouter()
for route in routeList:
    router.register(route[0], route[1], basename='movies')

urlpatterns = router.urls