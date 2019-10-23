from .common import Common


class production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn",)
