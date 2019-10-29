from django.core.management.base import BaseCommand, CommandError
from app_genres.models import Genre
from app_movies.models import Movie
import random


class Command(BaseCommand):
    help = "Fills a random number of genres on movies withouth genres"

    def add_arguments(self, parser):
        parser.add_argument(
            "--cleanup",
            default=False,
            action="store_true",
            help="Cleanup relations",
        )
        parser.add_argument(
            "--max_genres", nargs="?", default=3, type=int, help="Max number of genres"
        )

    def get_max_random_genres(self, max_genres):
        _max = random.randint(1, max_genres)
        return Genre.objects.order_by('?')[:_max]

    def handle(self, *args, **options):
        cleanup = options["cleanup"]
        max_genres = options["max_genres"]
        if cleanup:
            Movie.genre.through.objects.all().delete()
        movies = Movie.objects.all()
        for movie in movies:
            genres = self.get_max_random_genres(max_genres)
            self.stdout.write("Adding %s" % (movie.id, ))
            movie.genre.set(genres)
            movie.save()

        self.stdout.write(self.style.SUCCESS("Task done"))
