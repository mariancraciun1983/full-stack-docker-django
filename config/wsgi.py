#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from os import environ
from configurations.wsgi import get_wsgi_application

if "DJENV" not in environ:
    raise RuntimeError("DJENV environment variable is missing")

environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings." + environ["DJENV"])
environ.setdefault("DJANGO_CONFIGURATION", environ["DJENV"])


application = get_wsgi_application()
