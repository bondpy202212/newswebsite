# For PC
# import os


# def run_celery(): 
#     os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
#     os.system('celery -A tasks worker --loglevel=info --pool=solo > celery_logs.txt 2>&1')


# if __name__ == '__main__':
#     run_celery()


# For VM
from celery import Celery

app = Celery('app1', broker='redis://localhost:6379/0')
app.autodiscover_tasks(['tasks'])

if __name__ == '__main__':
    app.start()