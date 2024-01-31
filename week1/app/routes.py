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
    print(labclasses)
    return render_template('index.html', pagetitle=pagetitle, user=user, labclasses=labclasses)