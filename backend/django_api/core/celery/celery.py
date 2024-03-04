import os

import requests
from django.conf import settings
from celery import Celery, shared_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_api.settings")

celery_app = Celery("core", broker=settings.CELERY_URL)
celery_app.autodiscover_tasks()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30, sync_movies.s(), name="test")


# celery_app.conf.beat_schedule = {
#     "run-every-10-seconds": {
#         "task": "sync_movies",
#         "schedule": 10,
#     }
# }


@shared_task
def ping():
    print("running ping!")
    return "pong!"


@shared_task
def sync_movies():
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
