from flask import Blueprint, redirect, flash, render_template
from flask_login import current_user, login_required

from webapp.news.models import News
from webapp.user.decorators import admin_required
from webapp.user.forms import LoginForm
from webapp.user.models import User
from webapp.utils import get_redirect_target



blueprint = Blueprint('admin', __name__, url_prefix='/admin')


# page for admin
# @app.route('/admin')
@blueprint.route('/')
# @login_required
@admin_required
def admin_index():
    if current_user.is_admin:
        flash('Hello admin! (admin/views)')
        title = 'This page is for Administrators only'
        name_user = User.query.filter(User.username.isnot(None)).all() 
        news_count = News.query.filter(News.text.isnot(None)).count()
        
        return render_template('admin/info.html', page_title=title, name_user=name_user, news_count=news_count)
    else:
        flash("You aren't admin.")

