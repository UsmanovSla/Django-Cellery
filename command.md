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




git add --all
git commit -m "Msg"
git push origin main