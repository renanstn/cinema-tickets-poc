from django.db import models

from core.models import BaseModel
from core import utils


class Cinema(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    director = models.CharField(max_length=255)
    synopsis = models.TextField()

    def __str__(self) -> str:
        return self.title


class Room(BaseModel):
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, related_name="rooms"
    )
    number = models.IntegerField()
    movie = models.ForeignKey(
        "Movie", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.cinema.name} - {self.number}"

    def generate_chairs(self):
        """
        Generates room chairs according to room layout.
        Each row has a letter;
        Each column has a number.
        """
        chairs = []
        letters = utils.alphabet_letters_generator()
        for _ in range(1, 11):
            letter = next(letters)
            chairs.append(
                Chair(
                    code=f"{letter}01".upper(),
                    room=self,
                )
            )
        Chair.objects.bulk_create(chairs)


class Chair(BaseModel):
    AVAILABLE = "available"
    RESERVED = "reserved"
    SOLD = "sold"
    STATUS = (
        (AVAILABLE, "Available"),
        (RESERVED, "Reserved"),
        (SOLD, "Sold"),
    )

    code = models.CharField(max_length=3)
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="chairs"
    )
    status = models.CharField(
        max_length=255, choices=STATUS, default=AVAILABLE
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

    def __str__(self) -> str:
        return f"{self.room} - {self.code}"

    def reserve(self):
        self.status = Chair.RESERVED
        self.save()

    def free(self):
        self.status = Chair.AVAILABLE
        self.save()
