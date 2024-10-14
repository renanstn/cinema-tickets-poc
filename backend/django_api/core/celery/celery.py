import os

from celery import Celery, shared_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_api.settings")

celery_app = Celery("core")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


# Schedule periodic tasks -----------------------------------------------------
from cinema.tasks import ping_cinema, sync_movies


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Add all app tasks to the scheduler.
    """
    sender.add_periodic_task(5, ping.s(), name="ping_core")
    # sender.add_periodic_task(30, sync_movies.s(), name="sync_movies")
    sender.add_periodic_task(10, ping_cinema.s(), name="ping_cinema_app")


@shared_task
def ping():
    return "pong!"
