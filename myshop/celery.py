import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

'''
Для запуска -----------Ю>
!!  celery -A myshop worker -l info --pool=solo

Второй вариант(не проверен)
!! pip install eventlet

celery -A <project_name> worker --loglevel=info -P eventlet
'''