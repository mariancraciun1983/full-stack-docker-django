import os
from .common import common

class local(common):
    if "DEBUG" in os.environ and common.str2bool(os.environ["DEBUG"]):
        DEBUG = True

    # Testing
    INSTALLED_APPS = common.INSTALLED_APPS + [
        'debug_toolbar',
    ]
    MIDDLEWARE = common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = common.INTERNAL_IPS + [
        '0.0.0.0/0',
    ]
