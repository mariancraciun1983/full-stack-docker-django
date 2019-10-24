import os
from .common import Common

class Local(Common):
    if "DEBUG" in os.environ and Common.str2bool(os.environ["DEBUG"]):
        DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar',
    ]
    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '10.10.10.1',
    ]
