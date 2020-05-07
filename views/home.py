from flask import Blueprint, render_template, redirect, url_for
home_blueprint = Blueprint('home', __name__, template_folder='templates')
from queries import *
from flask import request
from flask_login import login_required, current_user
from queries import build_sets_private

@home_blueprint.route('/')
def root():
    return redirect(url_for('home.home'))

@home_blueprint.route('/home')
def home():
    public_sets = build_sets_public(current_user)
    private_sets = build_sets_private(current_user) if current_user.is_authenticated else None
    users = {}
    if current_user.is_authenticated:
        users[current_user.id] = current_user
    for set in public_sets:
        if set.user not in users:
            users[set.user] = db.session.query(User).filter_by(id=set.user).one()
    return render_template('home.html', public_sets=public_sets, private_sets=private_sets, current_user=current_user, users=users)

@home_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_set():
    if request.method == 'POST':
        process_form(request.form, current_user)
        return redirect(url_for('home.home'))
    return render_template('create.html')

@home_blueprint.route('/<int:user_id>/<string:username>')
def profile(user_id, username):
    user = User.query.filter_by(id=user_id).one()
    sets = build_sets_private(user)
    return render_template('profile.html', user=user, sets=sets)
