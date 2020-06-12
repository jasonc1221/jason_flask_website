from flask import render_template
from app import app

import datetime

@app.route('/')
@app.route('/index')
def index():
    age = int((datetime.date.today() - datetime.date(1996, 12, 21)).days / 365)
    return render_template('index.html', title='Home', age=age)