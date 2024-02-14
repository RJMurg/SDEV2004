from flask import Flask
from flask_babel import Babel

def get_locale():
    return 'ru'

app = Flask(__name__, template_folder="templates")
babel = Babel(app, locale_selector=get_locale)

from app import routes
