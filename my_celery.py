import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Message_service.settings')

from django.conf import settings

from celery import Celery

app = Celery('tasks', broker=f"{settings.REDIS_URL}")
