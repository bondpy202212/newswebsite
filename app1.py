# For PC
# import os


# def run_celery(): 
#     os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
#     os.system('celery -A tasks worker --loglevel=info --pool=solo > celery_logs.txt 2>&1')


# if __name__ == '__main__':
#     run_celery()


# For VM
import os
from tasks import celery_app

if __name__ == '__main__':
    # Set the FORKED_BY_MULTIPROCESSING environment variable
    os.environ['FORKED_BY_MULTIPROCESSING'] = '1'

    # Construct the command to be executed with shell redirection
    command = "celery -A tasks worker --loglevel=info --pool=solo >> celery_logs.txt 2>&1"

    # Execute the command using os.system()
    os.system(command)