import os


class Config:
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root!$23@localhost/flashcards'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
