from celery import Celery


app = Celery('task', broker_connection_retry_on_startup=True)
app.config_from_object('celeryconfig')

app.conf.imports = ('cwoker.tasks')
app.autodiscover_tasks()

# @app.task
# def add_numbers():
#     return
