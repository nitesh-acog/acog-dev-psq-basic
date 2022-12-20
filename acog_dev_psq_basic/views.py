from django.shortcuts import render
import json
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
#from django.core.mail import send_mail

from django_celery_beat.models import PeriodicTask,CrontabSchedule
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# minute='30',
#     hour='*',
#     day_of_week='*',
#     day_of_month='*',
#     month_of_year='*',
@csrf_exempt 
def API(request):
    if request.method=="POST":
        infile_path=request.POST.get('infile')
        print(request.POST)
        # print(infile_path)
        outfile_path=request.POST.get('outfile')
        # print(outfile_path)
        scheduleT,created=CrontabSchedule.objects.get_or_create(
            minute='*/1',
            hour='*',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',)

        
        uname=(str(datetime.now())).replace(' ','_').replace(':','_')
    task=PeriodicTask.objects.create(crontab=scheduleT,name=uname,task='acog_dev_psq_basic.tasks.process_infile',args=json.dumps((infile_path,outfile_path)),)

    
    
        
    return HttpResponse('Task has been push to Django ORM DB ready to be Scheduled ')


