from flask import Flask, session
from flask_babel import Babel

#This will set the language variable in session for the Babel app
def get_locale():
    if 'language' in session:
        return session['language']
    else:
        session['language']='en'
        return session['language']

#Create the flask app
app = Flask(__name__)
app.secret_key='AqTHAQRWWd5hJ7aPz95YAeCaNW4HTHEmxqxRp8tEB7ZimtKFP7VhipJVyxNiaBhDrJuCa4yBWFrJEqkbvoD'

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

from app import routes