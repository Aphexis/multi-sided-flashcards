from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)
import models
migrate = Migrate(app, db)


# app.config.from_object('config.Config')
from views.home import home_blueprint
from views.set import set_blueprint
from views.api import api_blueprint
from views.auth import auth_blueprint

app.register_blueprint(home_blueprint, url_prefix = '/test')
app.register_blueprint(set_blueprint, url_prefix = '/set')
app.register_blueprint(api_blueprint, url_prefix = '/api')
app.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    app.run()
