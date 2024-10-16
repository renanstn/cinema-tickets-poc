from django.urls import path, include
from rest_framework import routers

from cinema.api import viewsets


router = routers.DefaultRouter()

router.register(r"ping", viewsets.PingCinemaViewSet, basename="ping")
router.register(r"cinemas", viewsets.CinemaViewSet, basename="cinemas")
router.register(r"rooms", viewsets.RoomViewSet, basename="rooms")
router.register(r"chairs", viewsets.CharViewSet, basename="chairs")
router.register(r"waitlists", viewsets.WaitlistViewSet, basename="waitlists")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "cinemas/<uuid:cinema_id>/rooms",
        viewsets.RoomsList.as_view(),
        name="list_rooms",
    ),
    path(
        "cinemas/<uuid:cinema_id>/rooms/<uuid:room_id>/chairs",
        viewsets.CharsList.as_view(),
        name="list_chairs",
    ),
]
