from celery import Celery


app = Celery('task', broker_connection_retry_on_startup=True)
app.config_from_object('celeryconfig')


@app.task
def add_numbers():
    return
