import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery",
             backend='redis://redis:6379/0',
             broker='redis://redis:6379/0',
             broker_connection_retry_on_startup=True,)
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    return


app.autodiscover_tasks()
