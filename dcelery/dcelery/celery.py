import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery",
             backend='redis://redis:6379/0',
             broker='redis://redis:6379/0',
             broker_connection_retry_on_startup=True,)
app.config_from_object("django.conf:settings", namespace="CELERY")


# @app.task
# def add_numbers():
#     return

# app.conf.task_routes = {'cwoker.tasks.*': {'queue': 'queue1'},
#                         'cwoker.tasks.task2': {'queue': 'queue2'}}

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

app.autodiscover_tasks()
