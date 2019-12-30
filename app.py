from flask import Flask
import os

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:' + os.environ.get('password') + '@localhost/flashcards')

from views.home import home_blueprint
from views.set import set_blueprint

app = Flask(__name__)
# app.config.from_object('config.Config')

app.register_blueprint(home_blueprint)
app.register_blueprint(set_blueprint, url_prefix = '/set')

if __name__ == '__main__':
    app.run()
