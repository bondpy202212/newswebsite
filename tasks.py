from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import getnews  


flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

# @celery_app.task
# def add(x, y):
# 	print('-- hello --')
# 	print(x + y)

@celery_app.task
def getnews_snippets():
	with flask_app.app_context():
		getnews.get_news_snippets()


@celery_app.task
def getnews_content():
	with flask_app.app_context():
		getnews.get_news_content()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	# sender.add_periodic_task(crontab(second='*/10'), getnews_snippets.s())
	# sender.add_periodic_task(crontab(second='*/10'), getnews_content.s())

	sender.add_periodic_task(crontab(minute='*/1'), getnews_snippets.s())
	sender.add_periodic_task(crontab(minute='*/1'), getnews_content.s())

	# sender.add_periodic_task(crontab(hour='*/24'), getnews_snippets.s())
	# sender.add_periodic_task(crontab(hour='*/24'), getnews_content.s())

	# sender.add_periodic_task(crontab(day_of_week='*', hour='0'), getnews_snippets.s())
	# sender.add_periodic_task(crontab(day_of_week='*', hour='0'), getnews_content.s())




if __name__=='__main__':
	with flask_app.app_context():
		getnews.get_news_snippets()
		getnews.get_news_content()


# # # ++++++++++++++++++++++++++++++++++
# # # for BOT
# # # ++++++++++++++++++++++++++++++++++

from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import getnews  


flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def getnews_snippets():
	with flask_app.app_context():
		getnews.get_news_snippets()

@celery_app.task
def getnews_content():
	with flask_app.app_context():
		getnews.get_news_content()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	sender.add_periodic_task(crontab(second='*/10'), getnews_snippets.s())
	sender.add_periodic_task(crontab(second='*/10'), getnews_content.s())


if __name__=='__main__':
	with flask_app.app_context():
		getnews.get_news_snippets()
		getnews.get_news_content()







# from webapp import weather_html

# if __name__=='__main__':
# 	with flask_app.app_context():
# 		weather_html.weather_by_city()




# from webapp import create_app
# from webapp.news.parsers import getnews  

# def getnews_snippets():
# 	with flask_app.app_context():
# 		getnews.get_news_snippets()

# def getnews_content():
# 	with flask_app.app_context():
# 		getnews.get_news_content()


# if __name__=='__main__':
# 	with flask_app.app_context():
# 		getnews.get_news_snippets()
# 		getnews.get_news_content()



# +++++++++++++++++++

# from celery import Celery
# from celery.schedules import crontab


# from webapp import create_app
# from webapp.news.parsers import getnews


# flask_app = create_app()
# celery_app = Celery('tasks', broker='redis://localhost:6379/0')


# @celery_app.task
# def getnews_snippets():
# 	with flask_app.app_context():
# 		getnews.get_news_snippets()


# @celery_app.task
# def hgetnews_content():
# 	with flask_app.app_context():
# 		getnews.get_news_content()


# @celery_app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
# 	sender.add_periodic_task(crontab(minute='*/1'), getnews_snippets.s())
# 	sender.add_periodic_task(crontab(minute='*/1'), getnews_content.s())


# if __name__ == '__main__':
#     celery_app.conf.update(imports=['app'])
#     celery_app.worker_main(['worker', '--beat'])

# +++++++++++++++++++