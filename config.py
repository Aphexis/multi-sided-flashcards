import os


class Config:
    # FLASK_DEBUG = True
    # DEVELOPMENT = True
    SECRET_KEY = 'temporary'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:PASSWORD@localhost/flashcards'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = 'postgres://khkqzrytiqfcem:10b16bd169df54e265bbaf400457307f4e237bed7bb779ce647522521214a025@ec2-52-86-73-86.compute-1.amazonaws.com:5432/da0jv9ga6mh287'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
