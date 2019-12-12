import functools
from django.test import TestCase
from django.urls import reverse
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode


class Views_Index(TestCase):
    """ Test the cart index"""

    fixtures = ["auth.User.json", "app_genres.json", "app_movies.json", "app_cart.json"]

    def test_guest(self):
        """ Simulate a guest and get an empty cart and redirect on post """
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["cart"])

        response = self.client.post(reverse("cart"))
        self.assertEqual(response.status_code, 302)

    def test_user(self):
        """ Simulate the user and the cart update """
        self.client.logout()
        loggedin = self.client.login(username="john@example.com", password="password")
        self.assertTrue(loggedin, "Ensure is logged in")
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["cart"])

        # Get the cart before
        cart = response.context["cart"]
        itemsWithMovies = cart.getItemsWithMovies()
        prev_qty = functools.reduce(
            lambda accum, item: accum + item.quantity, itemsWithMovies, 0
        )
        self.assertEqual(prev_qty, 6)

        # update qty and remove a movie
        form_data = {
            "movie[]": [
                "03b98234-d848-4055-965a-50d9a2d6b1dc",
                "539c4409-6ca6-417b-9ed7-76a86b71a725",
                "f3cbff74-f55d-4164-9c7c-901da24253e0",
                "55704ae1-a310-4828-a166-31229ebc297e",
            ],
            "quantity[]": [2, 4, 5, 0],
        }
        response = self.client.post(
            reverse("cart"),
            urlencode(MultiValueDict(form_data), doseq=True),
            content_type="application/x-www-form-urlencoded",
        )
        # check cart before and after update

        self.assertEqual(response.status_code, 200)
        cart = response.context["cart"]
        itemsWithMovies = cart.getItemsWithMovies()
        new_qty = functools.reduce(
            lambda accum, item: accum + item.quantity, itemsWithMovies, 0
        )
        self.assertEqual(new_qty, 11)
        self.assertEqual(len(itemsWithMovies), 3)

        # Not sure if this i needed
        self.client.logout()
