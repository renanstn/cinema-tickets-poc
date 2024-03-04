from rest_framework.routers import DefaultRouter

from core.api.viewsets import PingViewSet

router = DefaultRouter()

router.register(r"ping", PingViewSet, basename="ping")
