from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Rupert Murdochtroyd'}
    return render_template('index.html', title='Lab Class Week 1', user=user)