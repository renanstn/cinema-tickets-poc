from rest_framework import routers
from cinema.api import viewsets


router = routers.DefaultRouter()

router.register("cinemas", viewsets.CinemaViewSet, basename="cinemas")
