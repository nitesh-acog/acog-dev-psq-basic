from celery import shared_task

from django_celery_beat.models import PeriodicTask, CrontabSchedule

# all one defines here is a task that needs to be pushed to the queue



@shared_task
def count_times(num:int)->None:
    for _ in range(num):
        print(num)