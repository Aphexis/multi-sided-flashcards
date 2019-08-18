from flask import Blueprint, render_template
from spreadsheet import *
from flashcard import Set

home_blueprint= Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def home():
    sets = get_all_sets()
    return render_template('home.html', sets=sets)

@home_blueprint.route('/set/<set_id>') # temporary
def set(set_id):
    return "you clicked set #" + str(set_id)
