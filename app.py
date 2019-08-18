from flask import Flask
from views.home import home_blueprint
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap = Bootstrap(app)
# app.config.from_pyfile('config.py')
# app.config.from_object("config.Config")
# app.config.update(
#     # TESTING=True,
#     DEBUG=True,
#     ENV='development'
# )
# print(app.config)
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True)