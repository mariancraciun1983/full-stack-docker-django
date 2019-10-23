from os import environ
from celery import Celery
import configurations


if "DJENV" not in environ:
    raise RuntimeError("DJENV environment variable is missing")

environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings." + environ["DJENV"])
environ.setdefault("DJANGO_CONFIGURATION", environ["DJENV"])

configurations.setup()

app = Celery("full-stack-django")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
