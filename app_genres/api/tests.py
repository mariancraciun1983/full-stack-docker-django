from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse


class Api_Views_ListViewSet(APITestCase):
    fixtures = ["app_genres.json"]

    def test_list(self):
        """Fetches the genres list"""
        response = self.client.get("/api/genres/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_retrieve(self):
        """Fetches the genre by id and by slug"""
        response = self.client.get("/api/genres/action/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["slug"], "action")

        response = self.client.get("/api/genres/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)

        self.assertEqual(len(response.data.keys()), 3)


class Api_Urls_Test(TestCase):
    def test_all_urls(self):
        """ Checks urls """
        url = reverse("api-genres--list")
        self.assertEqual(url, "/api/genres/")

        url = reverse("api-genres--detail", kwargs={"pk": 1})
        self.assertEqual(url, "/api/genres/1/")
