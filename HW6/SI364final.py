import os, json, datetime, requests
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'secretstringhere'

#postgresql://localhost/YOUR_DATABASE_NAME
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:icedout@localhost:5432/SI364projectplanCHALSEO"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager=Manager(app)
db=SQLAlchemy(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    db.create_all()
    manager.run()
