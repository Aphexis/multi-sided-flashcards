from flask import Blueprint, render_template, redirect, url_for, redirect
home_blueprint = Blueprint('home', __name__, template_folder='templates')
from sqlalchemy.orm import sessionmaker
from ..queries import *
from flask import request

@home_blueprint.route('/')
def root():
    return redirect(url_for('home.home'))

@home_blueprint.route('/home')
def home():
    Session = sessionmaker(bind=engine)
    session = Session()
    sets = build_sets(session)
    return render_template('home.html', sets=sets)

@home_blueprint.route('/create', methods=['GET', 'POST'])
def create_set():
    # form = CreateSet()
    # if form.validate_on_submit():
    #     return redirect(url_for('submitted'))
    if request.method == 'POST':
        set_id = process_form(request.form)
        print(set_id)
        return "set created!"
        # return request.form['name'] + request.form['description'] + request.form['sidename[0]'] + request.form['sidename[1]']
        # return request.form
    return render_template('create.html')

# @home_blueprint('/submitted', methods=['GET', 'POST'])
# def submitted():
#     return request.form['name'] + request.form['description']
