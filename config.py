import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////home/alexander/source/scoreboard/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSWORD_KEY = os.environ.get('PASSWORD_KEY') or 'password'
