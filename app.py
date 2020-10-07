from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from sqlalchemy import exc

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views.home import home_blueprint
from views.set import set_blueprint
from views.api import api_blueprint
from views.auth import auth_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(set_blueprint, url_prefix = '/set')
app.register_blueprint(api_blueprint, url_prefix = '/api')
app.register_blueprint(auth_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500_error.html'), 500

@app.errorhandler(exc.SQLAlchemyError)
def sql_alchemy_error(e):
    print(e)
    return render_template('500_error.html'), 500

if __name__ == '__main__':
    app.run()
