from django.db import models


class Genre(models.Model):
    """ Genre model """

    name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
