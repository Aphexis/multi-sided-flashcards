from flask import Flask
from views.home import home_blueprint

app = Flask(__name__)
# app.config.from_pyfile('config.py')
# app.config.from_object("config.Config")
# app.config.update(
#     # TESTING=True,
#     DEBUG=True,
#     ENV='development'
# )
# print(app.config)
app.register_blueprint(home_blueprint, url_prefix='/home')





if __name__ == '__main__':
    app.run(debug=True)
