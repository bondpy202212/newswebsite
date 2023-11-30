import os


def run_celery_beat():
    os.system('celery -A tasks beat')


if __name__ == '__main__':
    run_celery_beat()