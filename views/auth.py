from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import User
from flask_login import current_user, login_user, logout_user
from forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from app import db
import random
auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

# @auth_blueprint.route('/')
# def index():
#     return redirect(url_for('home.home'))

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', "error")
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.home')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    flash("You are now logged out!", "success")
    return redirect(url_for('home.home'))

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    avatars = {0: 'avatar lightblue', 1: 'avatar lightgreen', 2: 'avatar lightviolet', 3: 'avatar orange',
               4: 'avatar pink', 5: 'avatar purple', 6: 'avatar red', 7: 'avatar yellow'}
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        avatar = avatars[random.randint(0, 7)]
        avatar_url = url_for('static', filename='avatars/' + avatar + '.png')
        user = User(name=form.username.data, email=form.email.data, avatar=avatar_url)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', "success")
        return redirect(url_for('auth.login'))
    return render_template('sign-up.html', title='Register', form=form)