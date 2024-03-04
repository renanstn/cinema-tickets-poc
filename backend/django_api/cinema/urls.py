from rest_framework import routers
from cinema.api import viewsets


router = routers.DefaultRouter()

router.register(r"cinemas", viewsets.CinemaViewSet, basename="cinemas")
router.register(r"rooms", viewsets.RoomViewSet, basename="rooms")
router.register(r"ping", viewsets.PingCinemaViewSet, basename="ping")
