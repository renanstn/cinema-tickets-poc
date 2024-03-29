from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, mixins
from rest_framework.decorators import action
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

    @action(detail=True, methods=["post"])
    def generate_chairs(self, request, pk=None):
        room = self.get_object()
        room.generate_chairs()
        return Response({"message": "Chairs generated!"})


class RoomsList(generics.ListAPIView):
    """
    Allows to list cinema rooms filtered by cinema.
    """

    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        cinema = get_object_or_404(models.Cinema, id=self.kwargs["cinema_id"])
        return cinema.rooms.all().order_by("number")


class ChairViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = models.Chair.objects.all()
    serializer_class = serializers.ChairSerializer

    @action(detail=True, methods=["PUT"])
    def reserve(self, request, pk=None):
        chair = self.get_object()
        chair.reserve()
        return Response({"message": "chair reserved"})

    @action(detail=True, methods=["PUT"])
    def free(self, request, pk=None):
        chair = self.get_object()
        chair.free()
        return Response({"message": "chair available"})
