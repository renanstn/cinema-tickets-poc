from unittest.mock import patch

from django.test import TestCase

from cinema import tasks, models


class TasksTests(TestCase):
    @patch("cinema.tasks.requests.get")
    def test_sync_movies(self, mock_get):
        # GIVEN ---------------------------------------------------------------
        mock_movies = [
            {
                "title": "Movie 1",
                "director": "Director 1",
                "synopsis": "Synopsis 1",
            },
            {
                "title": "Movie 2",
                "director": "Director 2",
                "synopsis": "Synopsis 2",
            },
        ]
        mock_get.return_value.json.return_value = mock_movies
        # WHEN ----------------------------------------------------------------
        tasks.sync_movies()
        # THEN ----------------------------------------------------------------
        movies_in_db = models.Movie.objects.all()
        self.assertEqual(len(movies_in_db), 2)
        for mock_movie in mock_movies:
            movie_in_db = movies_in_db.get(title=mock_movie["title"])
            self.assertEqual(movie_in_db.director, mock_movie["director"])
            self.assertEqual(movie_in_db.synopsis, mock_movie["synopsis"])
