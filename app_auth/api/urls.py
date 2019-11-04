from rest_framework import routers
from .views import RegisterView, LoginView, ForgotView, ChangeView

routeList = (
    ('login', LoginView),
    ('register', RegisterView),
    ('forgot', ForgotView),
    ('change', ChangeView),
)

router = routers.DefaultRouter()
for route in routeList:
    router.register(route[0], route[1], basename='auth-'+route[0])

urlpatterns = router.urls
