from celery import shared_task


@shared_task
def ping_cinema():
    return "pong from cinema app!"


# @shared_task
# def sync_movies():
#     pass
