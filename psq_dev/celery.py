import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','psq_dev.settings')
# include =['acog_dev_psq_basic.tasks',]

app=Celery('psq_dev')

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')


