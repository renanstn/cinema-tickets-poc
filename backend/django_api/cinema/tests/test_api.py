from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from cinema import models


class CinemaTests(APITestCase):
    def setUp(self) -> None:
        """
        Authenticate on API.
        """
        user = User.objects.create_user(username="testuser")
        self.client.force_authenticate(user=user)

    def test_list_rooms(self):
        """
        It must be possible to list all cinema rooms using the URL:
        `/api/cinema/cinemas/<cinema_id>/rooms`
        """
        # GIVEN ---------------------------------------------------------------
        cinema_01 = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        cinema_02 = models.Cinema.objects.create(
            name="cinema 02", address="addr test 02"
        )
        room_01 = models.Room.objects.create(cinema=cinema_01, number=1)
        room_02 = models.Room.objects.create(cinema=cinema_01, number=2)
        models.Room.objects.create(cinema=cinema_02, number=1)
        # WHEN ----------------------------------------------------------------
        url = reverse("list_rooms", kwargs={"cinema_id": cinema_01.id})
        response = self.client.get(url)
        # THEN ----------------------------------------------------------------
        # Only cinema 01 rooms must be returned, ordered by room number
        self.assertEquals(
            response.json(),
            [
                {
                    "id": str(room_01.id),
                    "number": room_01.number,
                    "movie": None,
                },
                {
                    "id": str(room_02.id),
                    "number": room_02.number,
                    "movie": None,
                },
            ],
        )

    def test_list_chairs(self):
        """
        It must be possible to list all room chairs using the URL:
        `/api/cinema/cinemas/<cinema_id>/rooms/<room_id>/chars`
        """
        # GIVEN ---------------------------------------------------------------
        cinema_01 = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        room_01 = models.Room.objects.create(cinema=cinema_01, number=1)
        for i in range(60):
            models.Chair.objects.create(code=i, room=room_01)
        # WHEN ----------------------------------------------------------------
        url = reverse(
            "list_chairs",
            kwargs={"cinema_id": cinema_01.id, "room_id": room_01.id},
        )
        response = self.client.get(url)
        # THEN ----------------------------------------------------------------
        self.assertEquals(60, len(response.json()))

    def test_reserve_chair(self):
        """
        It must be possible to reserve a chair through the /reserve endpoint
        """
        # GIVEN ---------------------------------------------------------------
        cinema = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        room = models.Room.objects.create(cinema=cinema, number=1)
        chair = models.Chair.objects.create(code="A01", room=room)
        # WHEN ----------------------------------------------------------------
        url = reverse("chairs-reserve-chair", kwargs={"pk": chair.id})
        response = self.client.post(url)
        # THEN ----------------------------------------------------------------
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chair.refresh_from_db()
        self.assertEquals(chair.status, models.Chair.RESERVED)

    def test_free_chair(self):
        """
        It must be possible to free a chair through the /free endpoint
        """
        # GIVEN ---------------------------------------------------------------
        cinema = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        room = models.Room.objects.create(cinema=cinema, number=1)
        chair = models.Chair.objects.create(
            code="A01", room=room, status=models.Chair.RESERVED
        )
        # WHEN ----------------------------------------------------------------
        url = reverse("chairs-free-chair", kwargs={"pk": chair.id})
        response = self.client.post(url)
        # THEN ----------------------------------------------------------------
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chair.refresh_from_db()
        self.assertEquals(chair.status, models.Chair.AVAILABLE)

    def test_join_waitlist(self):
        """
        It must be possible to join the waitlist when a room is full
        """
        # GIVEN ---------------------------------------------------------------
        cinema = models.Cinema.objects.create(
            name="cinema 01", address="addr test 01"
        )
        room = models.Room.objects.create(cinema=cinema, number=1)
        chair = models.Chair.objects.create(
            code="A01", room=room, status=models.Chair.RESERVED
        )
        # WHEN ----------------------------------------------------------------
        url = reverse("waitlists-list")
        response = self.client.post(url, {"user_email": "test@test.com", "room": room.id})
        # THEN ----------------------------------------------------------------
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
