from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, mixins, status
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


class RoomsList(generics.ListAPIView):
    """
    Allows to list cinema rooms filtered by cinema.
    """

    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        cinema = get_object_or_404(models.Cinema, id=self.kwargs["cinema_id"])
        return cinema.rooms.all().order_by("number")


class CharsList(generics.ListAPIView):
    """
    Allows to list room chairs filtered by cinema and room.
    """

    serializer_class = serializers.ChairSerializer

    def get_queryset(self):
        cinema = get_object_or_404(models.Cinema, id=self.kwargs["cinema_id"])
        room = cinema.rooms.get(id=self.kwargs["room_id"])
        return room.chairs.all().order_by("code")


class CharViewSet(viewsets.ViewSet):
    @action(detail=True, methods=["POST"])
    def reserve_chair(self, request, pk=None):
        chair = get_object_or_404(models.Chair, id=pk)
        if chair.status != models.Chair.AVAILABLE:
            return Response(
                {"error": "Chair is already reserved"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        chair.reserve()
        return Response({"message": f"Chair {chair.code} reserved"})

    @action(detail=True, methods=["POST"])
    def free_chair(self, request, pk=None):
        chair = get_object_or_404(models.Chair, id=pk)
        chair.free()
        return Response({"message": f"Chair {chair.code} is available"})
