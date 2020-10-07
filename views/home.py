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
    public_sets_all = build_sets_public(current_user)
    public_sets = []
    private_sets = build_sets_private(current_user) if current_user.is_authenticated else None
    users = {}
    if current_user.is_authenticated:
        users[current_user.id] = current_user
        for set in public_sets_all:
            if set.user != current_user.id:
                public_sets.append(set)
    else:
        public_sets = public_sets_all
    for set in public_sets:
        if set.user not in users:
            users[set.user] = db.session.query(User).filter_by(id=set.user).one()
    return render_template('home.html', public_sets=public_sets, private_sets=private_sets, current_user=current_user, users=users)

@home_blueprint.route('/mysets')
@login_required
def my_sets():
    private_sets = build_sets_private(current_user)
    users = {}
    users[current_user.id] = current_user
    return render_template('all-sets.html', sets=private_sets, users=users, public=False)

@home_blueprint.route('/publicsets')
def public_sets():
    public_sets = build_sets_public(current_user)
    users = {}
    for set in public_sets:
        if set.user not in users:
            users[set.user] = db.session.query(User).filter_by(id=set.user).one()
    return render_template('all-sets.html', sets=public_sets, users=users, public=True)


@home_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_set():
    if request.method == 'POST':
        process_form(request.form, current_user)
        return redirect(url_for('home.home'))
    return render_template('create.html')

@home_blueprint.route('/profile/<string:username>')
def profile(username):
    user = User.query.filter(User.name.ilike(username)).first()
    if not user:
        return render_template('not_found.html')
    sets = build_sets_private(user)
    your_profile = True if current_user.is_authenticated and username == current_user.name else False
    return render_template('profile.html', user=user, sets=sets, your_profile=your_profile)

@home_blueprint.route('/not-found')
def not_found():
    return render_template('not_found.html')

@home_blueprint.route('/error')
def error():
    return render_template('500_error.html')