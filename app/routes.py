from flask import render_template,flash,redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'OxfordHack'}
    return render_template('index.html', title='Home', user=user)
