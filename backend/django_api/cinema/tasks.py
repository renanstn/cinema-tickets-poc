import os

import requests
from celery import shared_task


@shared_task
def ping_cinema():
    return "pong from cinema app!"


@shared_task
def sync_movies():
    """
    Sync movies from a third-party API to Movie model.
    """
    from cinema import models

    url = os.getenv("MOVIES_API_URL")
    movies = requests.get(url).json()

    for movie in movies:
        models.Movie.objects.update_or_create(
            title=movie["title"],
            defaults={
                "director": movie["director"],
                "synopsis": movie["synopsis"],
            },
        )


@shared_task
def check_expired_chairs():
    """
    Check and free expired reserved chairs.
    """
    from cinema import models
    from datetime import datetime

    for chair in models.Chair.objects.filter(hold_until__lt=datetime.now()):
        chair.free()
        # TODO: Check wait list and mail them!
