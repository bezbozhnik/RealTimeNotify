import os

from celery import Celery
from . import config
from django.conf import settings
# Создание экземпляра приложения Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtimenotify.settings')
app = Celery('app',
             broker=f'{config.CELERY_BROKER_URL}')

# Автоматическое обнаружение и регистрация задач Celery из модулей Django
app.autodiscover_tasks(settings.INSTALLED_APPS)

# Настройка работы Celery с Django
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

