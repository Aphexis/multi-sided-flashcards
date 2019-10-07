from flask import Blueprint, render_template
from spreadsheet import *
from flashcard import Set

set_blueprint= Blueprint('set', __name__, template_folder='templates')

@set_blueprint.route('/<int:set_id>') 
def set(set_id):
    set = get_set(set_id)
    # return "you clicked set #" + str(set_id)
    return render_template('set.html', set=set)

@set_blueprint.route('/<int:set_id>/edit')
def edit(set_id):
    set = get_set(set_id)
    return render_template('set-edit.html', set=set)

@set_blueprint.route('/<int:set_id>/view')
def view(set_id):
    set = get_set(set_id)
    return render_template('set-view.html', set=set)