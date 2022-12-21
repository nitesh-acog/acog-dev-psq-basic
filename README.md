```
these are few installations for the API

Django
celery
```
```
django-admin startproject psq-dev
```
Start the webserver
```
python manage.py runserver
```
Start the Celery worker
```
celery -A psq_dev.celery worker --pool=solo -l info
```
Start the celery beat
```
celery -A psq_dev beat -l info
```
# producer is anything that pushes item to to the Queue
# Queue here is a in-memory persistant service called Redis
# Consumer here is a celery worker that takes tasks from Redis
# An Api call pushes the task to DJango ORM DB
# Celery beat takes the periodic tasks from Django ORM Db and pushes it to the Queue(Redis)



