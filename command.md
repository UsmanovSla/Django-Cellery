python -m venv venv
venv\scripts\activate.bat 
pip install django
django-admin startproject dcelery
cd decelery
pip freeze > requirements.txt
pip install celery
pip install redis

docker-compose up -d --build


docker exec -it django /bin/sh
python manage.py startapp taskapp
python manage.py shell

from cwoker.tasks import sharedtask
sharedtask.delay()

from cwoker.tasks import task1, task2
task1.delay()
task2.delay()

from cwoker.tasks import tp1, tp2, tp3, tp4

tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()

git add --all
git commit -m "Msg"
git push origin main