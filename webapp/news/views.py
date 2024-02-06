from flask import abort, Blueprint, current_app, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.db import db
from webapp.news.forms_commit import CommentForm
from webapp.news.models import Comment, News
from webapp.weather_html import weather_by_city 
from webapp.utils import get_redirect_target


blueprint = Blueprint('news', __name__)


# @app.route('/')                                                 # start flask's object -> app
@blueprint.route('/') 
def index():
    title = current_app.config['PAGE_TITLE']
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])                       # go function weather
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()  # go function news
    city_name = current_app.config['WEATHER_DEFAULT_CITY']
    return render_template('news/index.html', page_title=title, weather = weather, city_name = city_name, news_list=news_list) # send to site


# text new's from DB to my site
@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()

    if not my_news:
        abort(404)
    comment_form = CommentForm(news_id=my_news.id)

    title = current_app.config['PAGE_TITLE']
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    city_name = current_app.config['WEATHER_DEFAULT_CITY']
    # print(comment_form.news_id)
    # return render_template('news/single_news.html', page_title=my_news.title, news=my_news, comment_form=comment_form, weather = weather, city_name = city_name)
    return render_template('news/single_news.html', page_title=title, news_title=my_news.title, news=my_news, comment_form=comment_form, weather = weather, city_name = city_name)


# page for comments
@blueprint.route('/news/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        # if News.query.filter(News.id == form.news_id.data).first():
        comment = Comment(text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment is added')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('ERROR in field "{}: - {}'.format(
                    getattr(form, field).label.text, 
                    error
                    ))
    return redirect(get_redirect_target())