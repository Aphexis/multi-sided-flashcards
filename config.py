import os


class Config:
    FLASK_DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'temporary'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:' + os.environ.get('password') + '@localhost/flashcards'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
