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
@login_required
def home():
    # Session = sessionmaker(bind=engine)
    # session = Session()
    sets = build_sets()
    return render_template('home.html', sets=sets)

@home_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_set():
    if request.method == 'POST':
        set_id = process_form(request.form)
        return redirect(url_for('home.home'))
    return render_template('create.html')
