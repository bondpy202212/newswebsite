# For PC
# import os


# def run_celery(): 
#     os.environ['FORKED_BY_MULTIPROCESSING'] = '1'
#     os.system('celery -A tasks worker --loglevel=info --pool=solo > celery_logs.txt 2>&1')


# if __name__ == '__main__':
#     run_celery()


# For VM

import sched
import time
import logging
from webapp import create_app
from webapp.news.parsers import getnews
import threading

# Создание объекта приложения Flask
flask_app = create_app()

def schedule_task():
    try:
        getnews.get_news_snippets()
        getnews.get_news_content()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Создание планировщика
scheduler = sched.scheduler(time.time, time.sleep)

# Планирование задачи для выполнения каждые 24 часа
scheduler.enter(0, 1, schedule_task)  # Запустить задачу сразу
scheduler.enter(10, 1, schedule_task)  # Запустить задачу через 10 секунд

# Логирование в файл
logging.basicConfig(filename='scheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Логирование запуска
logging.info('Scheduler started')

if __name__ == '__main__':
    # Запуск приложения Flask на порту 5001 в отдельном потоке
    app_thread = threading.Thread(target=flask_app.run, kwargs={'port': 5001})
    app_thread.start()

    # Запуск планировщика
    scheduler.run()

    print('start')

# Ожидание завершения потока сервера Flask
app_thread.join()

# Логирование завершения
logging.info('Scheduler stopped')




# import os
# # import locale

# # Set the locale to 'C'
# # locale.setlocale(locale.LC_TIME, 'C')

# from tasks import celery_app

# if __name__ == '__main__':
#     # Set the FORKED_BY_MULTIPROCESSING environment variable
#     os.environ['FORKED_BY_MULTIPROCESSING'] = '1'

#     # Construct the command to be executed with shell redirection
#     # command = "celery -A tasks worker --loglevel=info --pool=solo >> celery_logs.txt 2>&1"
#     command = "celery -A tasks worker --loglevel=info --pool=solo"

#     # Execute the command using os.system()
#     os.system(command)