import logging
from datetime import datetime

from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import getnews

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

# Настройка логирования для записи в файл
log_file_name = 'app.log'
logging.basicConfig(filename=log_file_name, level=logging.INFO)

@celery_app.task
def getnews_snippets():
    with flask_app.app_context():
        getnews.get_news_snippets()
        logging.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

@celery_app.task
def getnews_content():
    with flask_app.app_context():
        getnews.get_news_content()
        logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

@celery_app.task
def test_function():
    with flask_app.app_context():   
        print('hello...')     
        logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(second='*/10'), getnews_snippets.s())
    sender.add_periodic_task(crontab(second='*/10'), getnews_content.s())
    # sender.add_periodic_task(crontab(second='*/10'), test_function.s())

# if __name__ == "__main__":
#     celery_app.start()

if __name__=='__main__':
    with flask_app.app_context():
        getnews.get_news_snippets()
        getnews.get_news_content()
        celery_app.start()
        
# for start gunicorn from terminal: gunicorn main:app --bind localhost:8000 --workers 4 --timeout 120 --log-level info





# # # ----------- 
# # # with schedule (not working in VM, procces schedule not started in supervisor)
# # # -----------  
# from schedule import every
# import time
# import threading
# import logging
# from datetime import datetime

# from webapp import create_app
# from webapp.news.parsers import getnews

# # Создание приложения Flask
# # flask_app = create_app()
# app = create_app()
# flask_app = app

# logging.basicConfig(level=logging.INFO)
# log = logging.getLogger(__name__)

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()
#         log.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()
#         log.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# def schedule_jobs():
#     while True:
#         every(10).seconds.do(getnews_snippets)
#         every(10).seconds.do(getnews_content)
#         time.sleep(10)  # Пауза перед выполнением следующей планировки

# if __name__ == '__main__':
#     t = threading.Thread(target=schedule_jobs)
#     t.start()
#     flask_app.run()




# from schedule import every, run_pending
# import time
# import logging
# from datetime import datetime

# from webapp import create_app
# from webapp.news.parsers import getnews

# # Создание приложения Flask
# flask_app = create_app()

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()
#         logging.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()
#         logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# # Настройка логирования для записи в файл
# log_file_name = 'app.log'
# logging.basicConfig(filename=log_file_name, level=logging.INFO)


# # # # workers = 1
# # # # bind = '0.0.0.0:8000'
# # # # timeout = 60

# # # ----------- 
# # # for testing
# # # -----------            
# # start = datetime.now()
# # getnews_snippets()
# # finish = datetime.now() - start
# # print(f"time run getnew: {finish}")
# # getnews_content()

# # every(10).seconds.do(getnews_snippets)   
# # time.sleep(5)
# # every(10).seconds.do(getnews_content)
# # -----------            

# # # -----------
# # # working version
# # # -----------
# # getnews_snippets()
# # time.sleep(60)
# # getnews_content()

# # every().day.at("12:00").do(getnews_snippets)
# # time.sleep(60)
# # every().day.at("12:00").do(getnews_content)
# # # -----------




# def app():
#     while True:
#         time.sleep(1)
#         run_pending()
        
        
# if __name__ == '__main__':
#     every(10).seconds.do(getnews_snippets) 
#     every(10).seconds.do(getnews_content)
    
#     while True:
#         app()




# # # ++++++++++++++++++++++++++++++++++
# # # for BOT
# # # ++++++++++++++++++++++++++++++++++
# from schedule import every, run_pending
# import time
# import logging
# from datetime import datetime

# from webapp import create_app
# from webapp.news.parsers import getnews

# # Создание приложения Flask
# flask_app = create_app()

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()
#         logging.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()
#         logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# # Настройка логирования для записи в файл
# log_file_name = 'app.log'
# logging.basicConfig(filename=log_file_name, level=logging.INFO)

# every(10).seconds.do(getnews_snippets) 
# every(10).seconds.do(getnews_content)

# def app():
#     while True:
#         run_pending()
#         time.sleep(1)
        
# if __name__ == '__main__':
#     app()


# getnews_snippets()
# getnews_content()




















# # ++++++++++++++++++++++++++++++++++
# # for PC
# # ++++++++++++++++++++++++++++++++++

# from schedule import every, run_pending
# import time
# import logging
# from datetime import datetime

# from webapp import create_app
# from webapp.news.parsers import getnews 


# # Создание приложения Flask
# flask_app = create_app()

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()
#         # logging.info(f'getnews_snippets executed at {datetime.now()}')
#         logging.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()
#         # logging.info(f'getnews_content executed at {datetime.now()}')
#         logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# if __name__ == '__main__':
#     # Настройка логирования для записи в файл
#     log_file_name = 'app.log'
#     logging.basicConfig(filename=log_file_name, level=logging.INFO)

#     workers = 1
#     bind = '0.0.0.0:8000'
#     timeout = 60

#     # -----------            for testing
#     # start = datetime.now()
#     # getnews_snippets()
#     # finish = datetime.now() - start
#     # print(f"time run getnew: {finish}")
#     # getnews_content()

#     # every(10).seconds.do(getnews_snippets)   
#     # time.sleep(5)
#     # every(10).seconds.do(getnews_content)
#     # -----------            


#     getnews_snippets()
#     time.sleep(60)
#     getnews_content()

#     every().day.at("12:00").do(getnews_snippets)
#     time.sleep(60)
#     every().day.at("12:00").do(getnews_content)

#     while True:
#         run_pending()
#         time.sleep(1)
