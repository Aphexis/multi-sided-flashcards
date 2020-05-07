from flask import Blueprint, render_template, redirect, url_for, flash, request
set_blueprint = Blueprint('set', __name__, template_folder='templates')
from sqlalchemy.orm import sessionmaker
from queries import get_set, delete_set, edit_form
from flask_login import current_user, login_required
from models import User

@set_blueprint.route('/<int:set_id>') 
def set(set_id):
    set = get_set(set_id)
    if current_user.is_authenticated and set.user == current_user.id:
        set_info = set.get_card_info()
        return render_template('set.html', set=set, set_info=set_info, view_only=False, user=user)
    elif set.public:
        user = User.query.filter_by(id=set.user).one()
        set_info = set.get_card_info()
        return render_template('set.html', set=set, set_info=set_info, view_only=True, user=user)
    else:
        flash("You are not authorized to view this set!", "error")
        return redirect(url_for('home.home'))

@set_blueprint.route('/<int:set_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(set_id):
    if request.method == 'POST':
        edit_form(request.form, set_id)
        return redirect(url_for('set.set', set_id=set_id))
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
