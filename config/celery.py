import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('full-stack-django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
