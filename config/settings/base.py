import os
from socket import gethostname, gethostbyname
from celery.schedules import crontab

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

SECRET_KEY = '-d3=(fka+!7d_f%6f28ipz9c_fz2(@#r@8m-kvfk047*=1d&p0'

if 'DEBUG' in os.environ and os.environ['DEBUG']:
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = [
    gethostname(),
    gethostbyname(gethostname()),
    ".s-r-v.net"
]

REDIS = 'redis://redis.service:6379'
CELERY_BROKER_URL = REDIS
CELERY_RESULT_BACKEND = REDIS
CELERY_CACHE_BACKEND = REDIS
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BEAT_SCHEDULE = {
    'hello': {
        'task': 'app.tasks.hello',
        'schedule': crontab(minute='*/30')  # execute every minute
    }
}
CELERY_TASK_ALWAYS_EAGER=False
CELERY_EMAIL_TASK_CONFIG = {
    'queue' : 'email',
    'rate_limit' : '50/m',  # * CELERY_EMAIL_CHUNK_SIZE (default: 10)
}
CELERY_EMAIL_TASK_CONFIG = {
    'name': 'djcelery_email_send',
    'ignore_result': True,
}

SESSION_COOKIE_NAME = '_sid' 

INTERNAL_IPS = ['10.0.0.0/8']

EMAIL_HOST = 'mailer.service'
EMAIL_PORT = 25
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'djcelery_email',
    'app'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fsd',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'mysql.service',
        'PORT': 3306,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
