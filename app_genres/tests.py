from django.test import TestCase
from django.urls import reverse
from .models import Genre

class Views_Listing(TestCase):
    fixtures = ["app_genres.json", "app_movies.json"]

    def test_default(self):
        """Returns the unfiltered list of movies and categories"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["activeGenre"])
        self.assertIsNone(response.context["search"])
        self.assertGreater(response.context["genres"].count(), 1)
        self.assertGreater(response.context["movies"].count(), 1)

    def test_search(self):
        """Searches for movies"""
        search = "1234XXX4321"
        response = self.client.get(reverse("home"), {"search": search})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["search"], search)
        self.assertGreater(response.context["genres"].count(), 1)
        self.assertEqual(response.context["movies"].count(), 0)

    def test_slug(self):
        """Filters by genre"""
        slug = "action"
        response = self.client.get(reverse("genres-genre", kwargs={"slug": slug}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["activeGenre"].slug, slug)
        self.assertGreater(response.context["genres"].count(), 1)
        self.assertGreater(response.context["movies"].count(), 1)


class Models_Test(TestCase):

    def test_string_representation(self):
        """ Checks Genre model """
        entry = Genre(name="Genre Name", slug="genre_slug")
        self.assertEqual(str(entry), entry.name)

class Urls_Test(TestCase):

    def test_all_urls(self):
        """ Checks URLs """
        url = reverse('home')
        self.assertEqual(url, '/')

        url = reverse("genres-genre", kwargs={"slug": 'someslug'})
        self.assertEqual(url, '/genre/someslug')
