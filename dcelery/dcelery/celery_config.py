import os
# import queue
from celery import Celery
from kombu import Exchange, Queue
# import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery",
             broker='amqp://admin:12345@rabbitmq:5672/',
             #  backend='redis://redis:6379/0',
             #  broker='redis://redis:6379/0',
             broker_connection_retry_on_startup=True,)
app.config_from_object("django.conf:settings", namespace="CELERY")

#  Priority with RabbitMQ
app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', routing_key='dead_letter'),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


base_dir = os.getcwd()
task_folder = os.path.join(base_dir, 'dcelery', 'celery_tasks')

# dynamic load tasks from dir: dcelery.celery_tasks
if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith('ex') and filename.endswith('.py'):
            module_name = f'dcelery.celery_tasks.{filename[:-3]}'
            module = __import__(module_name, fromlist=['*'])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith('my_tasks'):
                    task_modules.append(f'{module_name}.{name}')

    app.autodiscover_tasks(task_modules)

# @app.task(queue='tasks')
# def t1(a, b, message=None):
#     time.sleep(3)
#     result = a + b
#     if message:
#         result = f'{message}: {result}'
#     return result


# @app.task(queue='tasks')
# def t2():
#     time.sleep(3)
#     return


# @app.task(queue='tasks')
# def t3():
#     time.sleep(3)
#     return

# # Limitation of one task
# # app.conf.task_default_rate_limit = '200/m'

# # @app.task
# # def add_numbers():
# #     return


# #  Queue wo RabbitMQ
# # app.conf.task_routes = {'cwoker.tasks.*': {'queue': 'queue1'},
# #                         'cwoker.tasks.task2': {'queue': 'queue2'}}


# #  Priority queue wo RabbitMQ

# # app.conf.broker_transport_options = {
# #     'priority_steps': list(range(10)),
# #     'sep': ':',
# #     'queue_order_strategy': 'priority',
# # }


# def test():
#     # Call the task asynchronously
#     result = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})

#     # Check if the task has completed
#     if result.ready():
#         print("Task has completed")
#     else:
#         print("Task is still running")

#     # Check if the task completed successfully
#     if result.successful():
#         print("Task completed successfully")
#     else:
#         print("Task encountered an error")

#     # Get the result of the task
#     try:
#         task_result = result.get()
#         print("Task result:", task_result)
#     except Exception as e:
#         print("An exception occurred:", str(e))

#     # Get the exception (if any) that occurred during task execution
#     exception = result.get(propagate=False)
#     if exception:
#         print("An exception occurred during task execution:", str(exception))


# # Synchronous task execution
# def execute_sync():
#     result = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})
#     task_result = result.get()
#     print("Task is running synchronously")
#     print(task_result)


# # Asynchronous task execution
# def execute_async():
#     result = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})
#     print("Task is running asynchronously")
#     print("Task ID:", result.task_id)
