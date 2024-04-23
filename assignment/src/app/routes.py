from app import app
from flask import render_template, session, redirect, request

@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en'  # Set default language here


@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))

@app.route('/routes')
def routes():
    return (render_template ("routes.html"))

@app.route('/discover')
def discover():
    return (render_template ("discover.html"))

@app.route('/shop')
def shop():
    return (render_template ("shop.html"))

@app.route('/planner')
def planner():
    return (render_template ("planner.html"))

@app.route('/map')
def map():
    return (render_template ("map.html"))

@app.route('/setlang/<lang_code>')
def set_language(lang_code):
#Pop the session variable to None to force an overwrite
    session.pop('language', None)
#Set the session variable lang to whatever code was used in the url
    session["language"] = lang_code
#refresh the page from which the set language request was made
    return redirect(request.referrer)
