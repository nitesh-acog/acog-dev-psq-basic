from django_celery_beat.models import PeriodicTask, CrontabSchedule

if __name__=='__main__':
    ScheduleT,created=CrontabSchedule.objects.get_or_create(hour=12,minute=48)
    PeriodicTask.objects.create(crontab=ScheduleT,name='tasksss',task='acog_dev_psq_basic.tasks.count_times')