from rest_framework import viewsets
from rest_framework.response import Response

from core.celery.celery import ping


class PingViewSet(viewsets.ViewSet):
    def list(self, request):
        ping.delay()
        return Response({"message": "pong!"})
