from flask import Blueprint, render_template, redirect, url_for
home_blueprint = Blueprint('home', __name__, template_folder='templates')

from queries import *

@home_blueprint.route('/')
def root():
    return redirect(url_for('home.home'))

@home_blueprint.route('/home')
def home():
    sets = build_sets()
    return render_template('home.html', sets=sets)
