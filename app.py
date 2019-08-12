from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.from_pyfile('config.py')

from hello import *

if __name__ == '__main__':
    app.run()