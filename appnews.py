from schedule import every, run_pending
import time
import logging
from datetime import datetime

from webapp import create_app
from webapp.news.parsers import getnews 


# Создание приложения Flask
flask_app = create_app()

def getnews_snippets():
    with flask_app.app_context():
        getnews.get_news_snippets()
        # logging.info(f'getnews_snippets executed at {datetime.now()}')
        logging.info(f'getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def getnews_content():
    with flask_app.app_context():
        getnews.get_news_content()
        # logging.info(f'getnews_content executed at {datetime.now()}')
        logging.info(f'getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

if __name__ == '__main__':
    # Настройка логирования для записи в файл
    log_file_name = 'app.log'
    logging.basicConfig(filename=log_file_name, level=logging.INFO)

    start = datetime.now()
    getnews_snippets()
    finish = datetime.now() - start
    print(f"time run getnew: {finish}")
    getnews_content()

    every(10).seconds.do(getnews_snippets)   
    time.sleep(5)
    every(10).seconds.do(getnews_content)

    # every().day.at("12:00").do(getnews_snippets)
    # time.sleep(10)
    # every().day.at("12:00").do(getnews_content)

    while True:
        run_pending()
        time.sleep(1)






# # ++++++++++++++++++++++++++++++++++
# # ++++++++++++++++++++++++++++++++++

# from schedule import every, run_pending
# import time
# import logging
# from datetime import datetime

# from webapp import create_app
# from webapp.news.parsers import getnews 



# flask_app = create_app()

# # def add(x, y):
# #     with flask_app.app_context():
# #         print('-- hello --')
# #         print(x + y)

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()
#         logging.info(f'getnews_snippets executed at {datetime.now()}')

# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()
#         logging.info(f'getnews_content executed at {datetime.now()}')

# # @app.route('/')
# # def index():
# #    return 'Hello, World!'


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger(__name__)


#     # Запускать задачу каждые 10 секунд
#     # every(1).seconds.do(add, 2, 3)
#     every(10).seconds.do(getnews_snippets)
#     every(10).seconds.do(getnews_content)
#     # -----------------------------
#     # every().day.at("12:00").do(add, 2, 3)

#     while True:
#         run_pending()
#         time.sleep(1)








# # ++++++++++++++++++++++++++++++++++
# # ++++++++++++++++++++++++++++++++++
# from schedule import every, run_pending
# import time

# from webapp import create_app
# from webapp.news.parsers import getnews 


# flask_app = create_app()

# def getnews_snippets():
#     with flask_app.app_context():
#         getnews.get_news_snippets()

# def getnews_content():
#     with flask_app.app_context():
#         getnews.get_news_content()


# if __name__ == '__main__':
#     # Запускать задачу каждые 10 секунд
#     every(10).seconds.do(add, 2, 3)

#     while True:
#         run_pending()
#         time.sleep(1)