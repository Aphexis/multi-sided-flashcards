from flask import Blueprint, render_template, redirect, url_for
from spreadsheet import *
from flashcard import Set

home_blueprint= Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def root():
    return redirect(url_for('home.home'))

@home_blueprint.route('/home')
def home():
    sets = get_all_sets()
    return render_template('home.html', sets=sets)