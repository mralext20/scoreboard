from flask import Flask
from config import Config
from flask_bs4 import Bootstrap
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes
