from flask import render_template
from app import app

import datetime

@app.route('/')
@app.route('/index')
def index():
    age = int((datetime.date.today() - datetime.date(1996, 12, 21)).days / 365)
    return render_template('index.html', title='Home', age=age)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title='About Me')

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')

@app.route('/contact_info')
def contact_info():
    return render_template('contact_info.html', title='Contact Info')