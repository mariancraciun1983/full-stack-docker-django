import sys
from os import path
from os.path import abspath, dirname, join, normpath
from socket import gethostname, gethostbyname
from celery.schedules import crontab
from configurations import Configuration

PROJECT_DIR = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(normpath(join(PROJECT_DIR, "apps")))


class Common(Configuration):
    @classmethod
    def str2bool(cls, v):
        return v.lower() in ("yes", "true", "t", "1")

    BASE_DIR = PROJECT_DIR

    SECRET_KEY = "-d3=(fka+!7d_f%6f28ipz9c_fz2(@#r@8m-kvfk047*=1d&p0"

    ALLOWED_HOSTS = [gethostname(), gethostbyname(gethostname()), ".s-r-v.net"]

    REDIS = "redis://redis.service:6379"
    CELERY_BROKER_URL = REDIS
    CELERY_RESULT_BACKEND = 'django-db'
    CELERY_CACHE_BACKEND = 'django-cache'
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    # CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
    CELERY_BEAT_SCHEDULE = {
        "hello": {
            "task": "app.tasks.hello",
            "schedule": crontab(minute="*/30"),  # execute every minute
        }
    }
    CELERY_TASK_ALWAYS_EAGER = False
    CELERY_EMAIL_TASK_CONFIG = {
        "queue": "email",
        "rate_limit": "50/m",  # * CELERY_EMAIL_CHUNK_SIZE (default: 10)
    }
    CELERY_EMAIL_TASK_CONFIG = {"name": "djcelery_email_send", "ignore_result": True}

    SESSION_COOKIE_NAME = "_sid"

    INTERNAL_IPS = ["10.0.0.0/8"]

    EMAIL_HOST = "mailer.service"
    EMAIL_PORT = 25
    EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"

    # Application definition
 
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django_celery_beat",
        "django_celery_results",
        "djcelery_email",
        "widget_tweaks",

        # Rest
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints

        # Your apps
        "app_cart",
        "app_genres",
        "app_movies",
    ]

    LOCAL_APPS = (
        # 'project.api'
    )

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "base.middleware.SetRemoteAddrMiddleware"
    ]

    ROOT_URLCONF = "config.urls"

    # TEMPLATES = [
    #     {
    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #         'DIRS': [],
    #         'APP_DIRS': True,
    #         'OPTIONS': {
    #             'context_processors': [
    #                 'django.template.context_processors.debug',
    #                 'django.template.context_processors.request',
    #                 'django.contrib.auth.context_processors.auth',
    #                 'django.contrib.messages.context_processors.messages',
    #             ],
    #         },
    #     },
    # ]

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                 'builtins': [
                    'app_cart.templatetags.cart_tags',
                ],
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.static",
                ]
            },
        }
    ]

    WSGI_APPLICATION = "config.wsgi.application"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "fsd",
            "USER": "user",
            "PASSWORD": "pass",
            "HOST": "mysql.service",
            "PORT": 3306,
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    # AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        )
    }

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        path.join(PROJECT_DIR, "static"),
    ]
