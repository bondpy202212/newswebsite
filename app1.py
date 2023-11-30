import os

def run_celery(): 
    os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
    os.system('celery -A tasks worker --loglevel=info --pool=solo > celery_logs.txt 2>&1')


if __name__ == '__main__':
    # with open('celery_logs.txt', 'w') as log_file:
    #     log_file.write('')
    run_celery()