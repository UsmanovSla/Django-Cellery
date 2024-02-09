<!-- venv -->
python -m venv venv
venv\scripts\activate.bat 


<!-- Django -->
django-admin startproject dcelery
python manage.py startapp taskapp

<!-- Pip -->
cd decelery
pip freeze > requirements.txt
pip install django
pip install celery
pip install redis

<!-- Docker build -->
docker-compose up -d --build

<!-- Remove all docker -->
<!-- Linux: PS or GIT -->
docker stop $(docker ps -qa) && docker rm $(docker ps -qa) && docker rmi $(docker images -qa)


<!-- Shell in Docker -->
docker exec -it django /bin/sh
python manage.py startapp taskapp
<!-- Python shell in Docker -->
python manage.py shell

<!-- Python command in shell in Docker -->
from cwoker.tasks import sharedtask
sharedtask.delay()

from cwoker.tasks import task1, task2
task1.delay()
task2.delay()

from celery import group
from cwoker.tasks import tp1, tp2, tp3, tp4
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

from celery import chain
from cwoker.tasks import tp1, tp2, tp3, tp4
task_chain = chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()

<!-- RabbitMQ + Docker Python shell -->
http://localhost:15672/#/

from dcelery.celery import t1
result = t1.apply_async(args=[5,10], kwargs={"message":"The sum is"})
print(result.get())

result.ready()
result.successful()

<!-- Celery -->
celery inspect active
celery inspect active_queues

<!-- RabbitQM with priority -->
<!-- RabbitMQ set new user with permission -->
rabbitmqctl add_user admin 12345
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

tp1.apply_async(priority=5)

<!--  Flower -->
http://localhost:5555/

<!-- Git -->
git add --all
git commit -m "Celery_Dynamic import task"
git push origin main