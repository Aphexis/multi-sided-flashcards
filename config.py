import os


class Config:
    # FLASK_DEBUG = True
    # DEVELOPMENT = True
    SECRET_KEY = 'temporary'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:PASSWORD@localhost/flashcards'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://gbjhictbcfhfuq:d603b46d58337bb54835aa4884c22992230d81d2cdfdd78c686cc9d20d1e6371@ec2-18-235-20-228.compute-1.amazonaws.com:5432/d8c92dutcoctfj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
