from schedule import every
import time
import threading
import logging
from datetime import datetime

from webapp import create_app
from webapp.news.parsers import getnews

# Создание приложения Flask
flask_app = create_app()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def getnews_snippets():
    with flask_app.app_context():
        getnews.get_news_snippets()
        log.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

def getnews_content():
    with flask_app.app_context():
        getnews.get_news_content()
        log.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

def schedule_jobs():
    while True:
        every(10).seconds.do(getnews_snippets)
        every(10).seconds.do(getnews_content)
        time.sleep(10)  # Пауза перед выполнением следующей планировки

if __name__ == '__main__':
    t = threading.Thread(target=schedule_jobs)
    t.start()
    app()




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

# getnews_snippets()
# getnews_content()

# def app():
#     while True:
#         run_pending()
#         time.sleep(1)
        
# if __name__ == '__main__':
#     app()






















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
