from flask import Blueprint, render_template, redirect, url_for
home_blueprint = Blueprint('home', __name__, template_folder='templates')
# from sqlalchemy.orm import sessionmaker
from queries import *
from flask import request
from flask_login import login_required, current_user

@home_blueprint.route('/')
def root():
    return redirect(url_for('home.home'))

@home_blueprint.route('/home')
def home():
    # Session = sessionmaker(bind=engine)
    # session = Session()
    public_sets = build_sets_public(current_user)
    private_sets = build_sets_private(current_user) if current_user.is_authenticated else None
    return render_template('home.html', public_sets=public_sets, private_sets=private_sets, current_user=current_user)

@home_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_set():
    if request.method == 'POST':
        process_form(request.form, current_user)
        return redirect(url_for('home.home'))
    return render_template('create.html')
