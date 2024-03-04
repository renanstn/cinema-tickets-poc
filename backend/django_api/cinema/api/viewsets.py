from rest_framework import viewsets
from rest_framework.response import Response

from cinema import models, tasks
from cinema.api import serializers


class PingCinemaViewSet(viewsets.ViewSet):
    def list(self, request):
        tasks.ping_cinema.delay()
        return Response({"message": "pong!"})


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = models.Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
