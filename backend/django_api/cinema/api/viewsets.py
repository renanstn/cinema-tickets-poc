from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
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


class RoomsList(generics.ListAPIView):
    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        cinema = get_object_or_404(models.Cinema, id=self.kwargs["cinema_id"])
        return cinema.rooms.all().order_by("number")
