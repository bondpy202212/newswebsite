from flask import Flask
from schedule import every, run_pending
import time

app = Flask(__name__)

def add(x, y):
   print('-- hello --')
   print(x + y)

# @app.route('/')
# def index():
#    return 'Hello, World!'

if __name__ == '__main__':
   # Запускать задачу каждые 10 секунд
   every(1).seconds.do(add, 2, 3)
   # every().day.at("12:00").do(add, 2, 3)

   while True:
       run_pending()
       time.sleep(1)
