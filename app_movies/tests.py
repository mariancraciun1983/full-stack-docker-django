from django.test import TestCase
from django.urls import reverse
from .models import Movie


class Views_Listing(TestCase):
    fixtures = ["app_movies.json"]

    def test_details(self):
        """Returns movie details"""
        uid = "0082832a-135e-4b3f-8210-c375d43fa88a"
        slug = "camera-buff-amator"
        response = self.client.get(
            reverse("movies-movie", kwargs={"id": uid, "slug": slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context["movie"].id), uid)


class Models_Test(TestCase):
    def test_string_representation(self):
        """ Checks the Movie model """
        title = "Camera Buff (Amator)"
        entry = Movie(
            title=title,
            slug="camera-buff-amator",
            description="Proin eu mi.",
            image="/static/images/movies/1.svg",
            price="7.41",
        )
        self.assertEqual(str(entry), title)

class Urls_Test(TestCase):

    def test_all_urls(self):
        """ Check the URLs """
        uid = "0082832a-135e-4b3f-8210-c375d43fa88a"
        slug = "camera-buff-amator"
        exp_url = "/movies/0082832a-135e-4b3f-8210-c375d43fa88a/camera-buff-amator"
        url = reverse("movies-movie", kwargs={"id": uid, "slug": slug})
        self.assertEqual(url, exp_url)
