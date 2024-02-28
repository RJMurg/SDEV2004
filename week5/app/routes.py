from app import app
from flask import render_template, session, redirect, request

@app.before_request
def set_session_language():
    if 'language' not in session:
        session["language"] = 'en'

@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))

@app.route('/about')
def about():
    return (render_template ("about.html"))

@app.route('/products')
def products():
        return (render_template ("products.html"))

@app.route('/store')
def store():
        return (render_template ("store.html"))
    
@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    session.pop('language', None)
    session["language"] = lang_code
    return redirect(request.referrer)