import os  
import logging
import time
from datetime import datetime

from webapp import create_app
from webapp.news.parsers import getnews  


flask_app = create_app()

log_file_name = 'app.log'
logging.basicConfig(filename=log_file_name, level=logging.INFO)


def test_func():
    with flask_app.app_context():
        # logging.info(f'test_function   : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        with open(log_file_name, 'w') as file:
            file.write(f'INFO:root:test_function: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


def getnews_snippets():
    with flask_app.app_context():
        getnews.get_news_snippets()
        with open(log_file_name, 'w') as file:
            file.write(f'INFO:root: getnews_snippets: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

def getnews_content():
    with flask_app.app_context():
        getnews.get_news_content()
        with open(log_file_name, 'a') as file:
            file.write(f'INFO:root: getnews_content : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')



# # # ----------- # # ----------- 
# # # start with gunicorn + supervisor
# @flask_app.route('/')
# def hello():
#     return 'Hello, World!'

# # start with gunicorn + supervisor
# if __name__ == "__main__" or "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
#     while True:
#         test_func()
#         time.sleep(10)




# # ----------- 
# # for file " appnews_gunicorn.conf" (supervisor)
# # -----------  
# logging.basicConfig(filename=log_file_name, filemode='w', level=logging.INFO)
# with open(log_file_name, 'w') as file:
        #     file.write(f'test_function: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
"""
sudo nano /etc/supervisor/conf.d/appnews_gunicorn.conf

[program:appnews_gunicorn]
command=/home/bondar1983ovdoc1/newswebsite/env/bin/gunicorn appnews:flask_app
directory=/home/bondar1983ovdoc1/newswebsite/
user=bondar1983ovdoc1
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/bondar1983ovdoc1/newswebsite/app_gunicorn.log


autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/user_name/newswebsite/app_flask.log


[program:appnews_gunicorn]
command=/home/user_name/newswebsite/env/bin/gunicorn appnews:flask_app
directory=/home/user_name/newswebsite/
user=user_name
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/user_name/newswebsite/app_gunicorn.log

"""
# # ----------- # # ----------- 




# # ----------- # # -----------
# # ----------- # # ----------- 
# # start with supervisor
if __name__ == "__main__":
    while True:
        # test_func()
        # time.sleep(10)

        getnews_snippets()
        getnews_content()
        # time.sleep(86400)
        time.sleep(43200)
# # ----------- # # -----------
# # ----------- # # ----------- 


# # ----------- 
# # for file " appnews.conf" (supervisor)
# # -----------  
"""
sudo nano /etc/supervisor/conf.d/appnews.conf

[program:appnews]
command=/home/bondar1983ovdoc1/newswebsite/env/bin/python /home/bondar1983ovdoc1/newswebsite/appnews.py
directory=/home/bondar1983ovdoc1/newswebsite
user=bondar1983ovdoc1
autostart=true
autorestart=true
startretries=3
redirect_stderr=true
stdout_logfile=/home/bondar1983ovdoc1/newswebsite/appnews_supervisor.log

startsecs=10
---------
sudo rm -r celery
sudo rm /etc/supervisor/conf.d/celery_worker.conf
sudo rm /etc/supervisor/conf.d/celery_beat.conf
---------

"""
# # ----------- # # ----------- 





