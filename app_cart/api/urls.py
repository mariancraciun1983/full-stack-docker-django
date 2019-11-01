from rest_framework import routers
from .views import CartViewSet

routeList = (
    ('', CartViewSet),
)

router = routers.DefaultRouter()
for route in routeList:
    router.register(route[0], route[1], basename='cart')

urlpatterns = router.urls
