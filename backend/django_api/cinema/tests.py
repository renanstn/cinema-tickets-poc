import uuid

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

from cinema import models


class CinemaTests(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username="testuser")
        self.client.force_authenticate(user=user)

    def test_list_rooms(self):
        """
        It must be possible to list all cinema rooms using the URL:
        `/api/cinema/cinemas/<cinema_id>/rooms`
        """
        # GIVEN
        cinema_01 = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        cinema_02 = models.Cinema.objects.create(
            name="cinema 02", address="addr test 02"
        )
        models.Room.objects.create(cinema=cinema_01, number=1)
        models.Room.objects.create(cinema=cinema_01, number=2)
        models.Room.objects.create(cinema=cinema_02, number=1)
        # WHEN
        url = reverse("list_rooms", kwargs={"cinema_id": cinema_01.id})
        response = self.client.get(url)
        # THEN
        # Only cinema 01 rooms must be returned
        self.assertEquals(len(response.json()), 2)
