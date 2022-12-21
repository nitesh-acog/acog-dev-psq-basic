from celery import shared_task
from django.http import HttpResponse
import os
import pandas as pd
import json

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from sqlite_ import SQLITE3


# all one defines here is a task that needs to be pushed to the queue


# @shared_task
# def count_times(num:int)->None:
#     for _ in range(num):
#         print(num)


@shared_task(bind=True)
def process_infile(self, path_: str, out_path: str) -> None:
    print(path_, out_path)

    sql = SQLITE3("sqlite3")
    print("Connected TO sqilte3")
    table_name = path_.replace("/", "_").replace("-", "_") + out_path.replace(
        "/", "_"
    ).replace("-", "_")
    print(table_name)
    infiles = os.listdir(path_)
    out_files = [x.replace('.csv','.html') for x in infiles]
    # file_in_path = [
    #     sql.check_if_both_infile_outfile_in_table(table_name, infile_, out_file_)
    #     for infile_, out_file_ in zip(infiles, out_files)
    # ]
    
    

    if not sql.check_for_table(table_name) :
        sql.create_table(table_name, "djedi")
        print("created table")

        print(infiles)
        if len(infiles) == 0:
            print("The input DIR here is empty")
        

        non_processed_files= [
            (infile, outfile)
            for infile, outfile in zip(infiles, out_files)
            if sql.check_if_both_infile_outfile_in_table(table_name, infile, outfile)
            == False
        ]
        

        non_processed_files_= [
            sql.check_if_both_infile_outfile_in_table(table_name, infile, outfile)
            for infile, outfile in zip(infiles, out_files)
        ]

        print(non_processed_files)
        for x in non_processed_files:
            sql.insert_record(table_name, x[0], x[1], status=0)
            print('Inserted in table')
        if len(non_processed_files) == 0:
            print("All files in given path are processed and available")
        for i, o in non_processed_files:
            try:
                os.makedirs(out_path, exist_ok=True)
                df = pd.read_csv(os.path.join(path_, i)).to_html(
                    os.path.join(out_path, o)
                )

                sql.update_table(table_name,i,o,1)
                print('Updated Status')
            except Exception as e:
                print(e)

                print("Found a file not able to prsed by pandas")

        print("The Task is Scheduled ")
    elif sql.check_for_table(table_name):
        

        non_processed_files= [
            (infile, outfile)
            for infile, outfile in zip(infiles, out_files)
            if sql.check_if_both_infile_outfile_in_table(table_name, infile, outfile)
            == False
        ]
    

        non_processed_files_= [
            sql.check_if_both_infile_outfile_in_table(table_name, infile, outfile)
            for infile, outfile in zip(infiles, out_files)
        ]

        if False in non_processed_files_:
         print(non_processed_files_)
         for i, o in non_processed_files:
            try:
                os.makedirs(out_path, exist_ok=True)
                df = pd.read_csv(os.path.join(path_, i)).to_html(
                    os.path.join(out_path, o)
                )
                print('File processed')
                sql.update_table(table_name,i,o,1)
                print('updated sql status')
                
            except Exception as e:
                print(e)

                print("Found a file not able to prsed by pandas")

    
    else:
        print(
            "The given input paths and output path already exists//||  \n try changing the output path for different destination or the input PATH"
        )
