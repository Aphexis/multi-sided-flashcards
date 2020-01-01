from flask import Flask
import os


#os.environ.get('password')
from views.home import home_blueprint
from views.set import set_blueprint

app = Flask(__name__)
# app.config.from_object('config.Config')

app.register_blueprint(home_blueprint)
app.register_blueprint(set_blueprint, url_prefix = '/set')

if __name__ == '__main__':
    app.run()
