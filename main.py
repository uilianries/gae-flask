import logging

from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

@app.route('/')
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    new_user = models.User(name=name, email=email, url=site, comments=comments)
    db.session.add(new_user)
    db.session.commit()

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

@app.route('/list')
def list():
    users = models.User.query.all()
    return render_template('list.html', users=users)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
