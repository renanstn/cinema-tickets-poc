from core.api.serializers import BaseSerializer
from cinema import models


class MovieSerializer(BaseSerializer):
    class Meta:
        model = models.Movie
        fields = ["id", "title", "director", "synopsis"]


class ChairSerializer(BaseSerializer):
    class Meta:
        model = models.Chair
        fields = ["id", "code", "status", "active"]


class RoomSerializer(BaseSerializer):
    movie = MovieSerializer()

    class Meta:
        model = models.Room
        fields = ["id", "number", "movie"]


class CinemaSerializer(BaseSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = models.Cinema
        fields = ["id", "name", "address", "rooms"]
