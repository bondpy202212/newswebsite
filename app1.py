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
    os.system('/home/bondar1983ovdoc1/newswebsite/env/bin/celery -A app1 worker --loglevel=info > celery_logs.txt 2>&1')

if __name__ == '__main__':
    run_celery()