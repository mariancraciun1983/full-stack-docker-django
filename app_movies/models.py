import uuid
from django.db import models
from app_genres.models import Genre


class Movie(models.Model):
    """ Movie model """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, unique=False, blank=False, null=False)
    slug = models.SlugField(max_length=128, unique=True, db_index=True, blank=False, null=False)
    genre = models.ManyToManyField(Genre, db_table='app_Movie_Genre')
    description = models.TextField(max_length=1024)
    image = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        db_table = 'app_Movie'
