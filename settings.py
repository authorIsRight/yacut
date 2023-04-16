import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', default='asidyfukahs23')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False