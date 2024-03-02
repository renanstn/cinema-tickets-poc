from rest_framework import serializers
from core.api.serializers import BaseSerializer
from cinema import models


class RoomSerializer(BaseSerializer):
    class Meta:
        model = models.Room
        fields = ["id", "number", "capacity"]


class CinemaSerializer(BaseSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = models.Cinema
        fields = ["id", "name", "address", "rooms"]
