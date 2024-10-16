from datetime import timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone

from core.models import BaseModel


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

    @classmethod
    def has_free_chairs(cls) -> bool:
        return cls.objects.filter(chairs__status=Chair.AVAILABLE).exists()


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
    hold_until = models.DateTimeField(
        null=True,
        blank=True,
        help_text=(
            "Time limit for a reservation. "
            "After this time the chair will be available again."
        ),
    )

    class Meta:
        ordering = ["code"]

    def __str__(self) -> str:
        return f"{self.room} - {self.code}"

    def reserve(self):
        self.status = Chair.RESERVED
        current_time = timezone.now()
        time_limit = current_time + timedelta(
            minutes=settings.WAITLIST_TIME_LIMIT
        )
        self.hold_until = time_limit
        self.save()

    def free(self):
        self.status = Chair.AVAILABLE
        self.save()


class Waitlist(BaseModel):
    user_email = models.CharField(max_length=255)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="waitlist"
    )
    join_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.room} - {self.user_email}"
