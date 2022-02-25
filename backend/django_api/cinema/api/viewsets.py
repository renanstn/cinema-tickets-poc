from rest_framework import viewsets
from cinema import models
from cinema.api import serializers


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = models.Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer
