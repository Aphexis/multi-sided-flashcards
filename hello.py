# from flask import Flask
from flask import render_template
# app = Flask(__name__)
from app import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
