from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.utils import get_redirect_target


blueprint = Blueprint('user', __name__, url_prefix='/users')


# user's form
@blueprint.route('/login')
def login():
    if current_user.is_authenticated:                   # if user authenticated
        # return redirect(url_for('news.index'))        # go start page
        return redirect(get_redirect_target())
    title = 'Authorization'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


# processing login
@blueprint.route('/process-login', methods=['POST'])
# @blueprint.route('/process-login')
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You are visiting the site!!')
            # return redirect(url_for('news.index'))
            return redirect(get_redirect_target())
        else:
            flash('Name or password not correct.')
            flash('(Caps Lock may be on)')

            return redirect(url_for('user.login'))
    

# user logout
@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You are leaving the site.')
    # return redirect(url_for('news.index'))
    return redirect(get_redirect_target())



# user registration
@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        # return redirect(url_for('news.index'))
        return redirect(get_redirect_target())
    form = RegistrationForm()
    title = 'Registration'
    return render_template('user/registration.html', page_title=title, form=form)


# processing registration
@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have registered!')
        return redirect(url_for('user.login'))
        
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('ERROR in field "{}: - {}'.format(
                    getattr(form, field).label.text, 
                    error
                    ))
        return redirect(url_for('user.register'))
    # flash('Please, enter correct data. (user/views.py)')
    # return redirect(url_for('user.register'))

