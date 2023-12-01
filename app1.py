# For PC
# import os


# def run_celery(): 
#     os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
#     os.system('celery -A tasks worker --loglevel=info --pool=solo > celery_logs.txt 2>&1')


# if __name__ == '__main__':
#     run_celery()


# For VM
import os

def run_celery():
    os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
    os.system('/home/user_name/newswebsite/env/bin/celery -A your_app_name worker --loglevel=info > celery_logs.txt 2>&1')

if __name__ == '__main__':
    run_celery()