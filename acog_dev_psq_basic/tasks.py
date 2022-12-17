from celery import shared_task

from django_celery_beat.models import PeriodicTask, CrontabSchedule

@shared_task
def count_times(num:int)->None:
    for _ in range(num):
        print(num)