from core.api.serializers import BaseSerializer
from cinema import models


class MovieSerializer(BaseSerializer):
    class Meta:
        model = models.Movie
        fields = ["id", "title", "director", "synopsis"]


class RoomSerializer(BaseSerializer):
    movie = MovieSerializer()

    class Meta:
        model = models.Room
        fields = ["id", "number", "movie"]


class CinemaSerializer(BaseSerializer):
    class Meta:
        model = models.Cinema
        fields = ["id", "name", "address"]
