from .common import common


class production(common):
    INSTALLED_APPS = common.INSTALLED_APPS
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn",)
