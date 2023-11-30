from datetime import datetime, timedelta
from flask import current_app
import locale
import platform

from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news


# for date formating local
# if platform.system() == 'Windows':
# 	locale.setlocale(locale.LC_ALL, "russian")
# else:
# 	locale.setlocale(locale.LC_TIME, 'ru_RU')


# for date formating local
if platform.system() == 'Windows':
	locale.setlocale(locale.LC_ALL, "en_US")
else:
	locale.setlocale(locale.LC_TIME, 'en_US')



# formation date "сегодня в 02:32" to '19 05 2023 02:32'
def parse_date(date_str):
	if 'today' in date_str:
		today = datetime.now()
		date_str = date_str.replace('today', today.strftime('%d %B %Y'))
	elif 'yesterday' in date_str:
		yesterday = datetime.now() - timedelta(days=1)
		date_str = date_str.replace('yesterday', yesterday.strftime('%d %B %Y'))
	try:
		# return datetime.strptime(date_str, '%d %b %Y в %H:%M:%S')
		return datetime.strptime(date_str, '%d %B %Y')
	except ValueError:
		# datetime1 = datetime.now()
		# return datetime1.strftime('%Y-%m-%d')
		return datetime.now()


# news from habr.com (title, ulr, date)
def get_news_snippets():
	html = get_html(current_app.config['HTTPS'])

	if html:
		soup = BeautifulSoup(html, 'html.parser')

		if current_app.config['ALL_NEWS'] == 0:
			all_news = soup.find('div', class_="grid-x grid-margin-x").findAll('article', class_='archive-post')
		elif current_app.config['ALL_NEWS'] == 1:
			all_news = soup.find('div', class_="tm-articles-list").findAll('article', class_='tm-articles-list__item')
		else:
			all_news = None
		# print(len(all_news))


		for news in all_news:
			if current_app.config['ALL_NEWS'] == 0:
				title = news.find('header', class_="article-header").a['title']
			elif current_app.config['ALL_NEWS'] == 1:
				title = news.find('a', class_="tm-title__link").text
			else:
				title = None
			

			if current_app.config['ALL_NEWS'] == 0:
				url = news.find('header', class_="article-header").a['href']
			elif current_app.config['ALL_NEWS'] == 1:
				url = news.find('a', class_="tm-title__link")['href']
			else:
				url = None


			if current_app.config['ALL_NEWS'] == 0:
				pass
			elif current_app.config['ALL_NEWS'] == 1:
				url = current_app.config['URL_PLUS'] + url
			else:
				url = None


			if current_app.config['ALL_NEWS'] == 0:
				published0 = news.find('div', class_="content").text
				published = published0.strip().split('|')[0].strip()
			elif current_app.config['ALL_NEWS'] == 1:
				published = news.find('span', class_="tm-article-datetime-published").text
				published0 = news.find('span', class_="tm-article-datetime-published")
				time_tag = published0.find('time')
				datetime_str = time_tag.get('datetime')
				date_time = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ')
				formatted_date = date_time.strftime('%d %b %Y в %H:%M')
				published = str(formatted_date)
			else:
				published = None			


			published = parse_date(published)
			
			# print('----------------------------')
			# print(title, url, published)
			# print(f"{title}\n{url}\n{published}")
			# print()
			# print('++++++++++++++++++++++++++++')

			save_news(title, url, published)


# text for news (take content from site)
def get_news_content():
	news_without_text = News.query.filter(News.text.is_(None))
	for news in news_without_text:
		html = get_html(news.url)
		if html:
			soup = BeautifulSoup(html, 'html.parser')

			if current_app.config['ALL_NEWS'] == 0:
				news_text = soup.find('div', class_='grid-x grid-margin-x margin-top-2').decode_contents()
				# news_text = soup.find('div', class_='cell small-12 medium-12 large-12').decode_contents()	
			elif current_app.config['ALL_NEWS'] == 1:
				news_text = soup.find('div', class_='article-formatted-body').decode_contents()
			else:
				news_text = None
			

					

			if news_text:
				news.text = news_text
				db.session.add(news)
				db.session.commit()

