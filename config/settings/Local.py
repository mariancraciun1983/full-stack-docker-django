import os
from .common import Common

class Local(Common):
    if "DEBUG" in os.environ and Common.str2bool(os.environ["DEBUG"]):
        DEBUG = True
    else:
        DEBUG = False

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
