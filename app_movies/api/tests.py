from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse


class Api_Views_ListViewSet(APITestCase):
    fixtures = ["app_movies.json"]

    def test_list(self):
        """Fetches the movies list"""
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_retrieve(self):
        """Fetches the movie by id"""
        uid = "0082832a-135e-4b3f-8210-c375d43fa88a"
        response = self.client.get("/api/movies/" + uid + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.data["id"]), uid)
        self.assertEqual(len(response.data.keys()), 7)


class Api_Urls_Test(TestCase):
    def test_all_urls(self):
        """ Checks the URLs """
        url = reverse("api-movies--list")
        self.assertEqual(url, "/api/movies/")
        uid = "0082832a-135e-4b3f-8210-c375d43fa88a"
        url = reverse("api-movies--detail", kwargs={"pk": uid})
        self.assertEqual(url, "/api/movies/" + uid + "/")
