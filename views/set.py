from flask import Blueprint, render_template, redirect, url_for, flash
set_blueprint = Blueprint('set', __name__, template_folder='templates')
from sqlalchemy.orm import sessionmaker
from queries import get_set, delete_set
from flask_login import current_user, login_required

@set_blueprint.route('/<int:set_id>') 
def set(set_id):
    set = get_set(set_id)
    if current_user.is_authenticated and set.user == current_user.id:
        set_info = set.get_card_info()
        return render_template('set.html', set=set, set_info=set_info, view_only=False)
    elif set.public:
        set_info = set.get_card_info()
        return render_template('set.html', set=set, set_info=set_info, view_only=True)
    else:
        flash("You are not authorized to view this set!", "error")
        return redirect(url_for('home.home'))

@set_blueprint.route('/<int:set_id>/edit')
@login_required
def edit(set_id):
    set = get_set(set_id)
    if current_user.is_authenticated and set.user == current_user.id:
        return render_template('set-edit.html', set=set)
    elif set.public:
        flash("You are not authorized to edit this set!", "error")
        return redirect(url_for('set.set', set_id=set_id))
    else:
        flash("You are not authorized to view this set!", "error")
        return redirect(url_for('home.home'))

@set_blueprint.route('/<int:set_id>/study')
def study(set_id):
    set = get_set(set_id)
    if set.public or (current_user.is_authenticated and set.user == current_user.id):
        return render_template('set-study.html', set=set)
    else:
        flash("You are not authorized to view this set!", "error")
        return redirect(url_for('home.home'))

@set_blueprint.route('/<int:set_id>/delete')
@login_required
def delete(set_id):
    set = get_set(set_id)
    if current_user.is_authenticated and set.user == current_user.id:
        delete_set(set_id)
        flash("Set '" + set.name + "' was deleted!", "success")
        return redirect(url_for('home.home'))
    elif set.public:
        flash("You are not authorized to delete this set!", "error")
        return redirect(url_for('set.set', set_id=set_id))
    else:
        flash("You are not authorized to view this set!", "error")
        return redirect(url_for('home.home'))
