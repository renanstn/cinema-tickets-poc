from django.db import models
from core.models import BaseModel


class Cinema(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Room(BaseModel):
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, related_name="rooms"
    )
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.cinema.name} - {self.number}"
