from django.db import models
from django.contrib.auth.models import User
from app_movies.models import Movie


class Cart(models.Model):
    """ Cart model """

    NEW = 'new'
    SUBMITTED = 'submitted'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (SUBMITTED, 'Submitted'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=NEW,
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateField(blank=False, auto_now_add=True)
    updated = models.DateField(blank=False, auto_now=True)

    def __str__(self):
        return self.id

    def getItemsWithMovies(self):
        return CartItems.objects.filter(cart=self).select_related('movie')

    class Meta:
        ordering = ('-id',)
        db_table = 'app_Cart'


class CartItems(models.Model):
    """ CartItems model """

    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField(default=1)
    added = models.DateField(blank=False, auto_now_add=True)
    updated = models.DateField(blank=False, auto_now=True)

    class Meta:
        ordering = ('cart', "movie",)
        unique_together = (("cart", "movie"),)
        db_table = 'app_CartItems'
