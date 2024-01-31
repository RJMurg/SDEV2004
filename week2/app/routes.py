from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Ruan Murgatroyd'}
    labclasses = [
        {
            'weekno': 'one',
            'content': 'Getting started with Flask!'
        },
        {
            'weekno': 'two',
            'content': 'Template Inheritance!'
        }
    ]
    pagetitle = "Lab TWO"
    return render_template('index.html', pagetitle=pagetitle, user=user, labclasses=labclasses)

@app.route('/labs')
def labs():
    return render_template('labs.html')

@app.route('/ca')
def ca():
    return render_template('ca.html')