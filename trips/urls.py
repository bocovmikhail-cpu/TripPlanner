from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TripViewSet, RegisterView

router = DefaultRouter()
router.register("trips", TripViewSet, basename="trip")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="register"),
]
