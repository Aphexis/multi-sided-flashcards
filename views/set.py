from flask import Blueprint, render_template
set_blueprint = Blueprint('set', __name__, template_folder='templates')

from queries import get_set

@set_blueprint.route('/<int:set_id>') 
def set(set_id):
    # sets = build_sets()
    set = get_set(set_id)
    set_info = set.get_card_info()
    # return "you clicked set #" + str(set_id)
    return render_template('set.html', set=set, set_info=set_info)

@set_blueprint.route('/<int:set_id>/edit')
def edit(set_id):
    set = get_set(set_id)
    return render_template('set-edit.html', set=set)

@set_blueprint.route('/<int:set_id>/view')
def view(set_id):
    set = get_set(set_id)
    return render_template('set-view.html', set=set)
