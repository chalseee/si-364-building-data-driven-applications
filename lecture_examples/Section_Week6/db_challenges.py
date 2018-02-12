import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_script import Shell, Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

# Configure base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

# Application configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstringfromsi364thisisnotsupersecurebutitsok'

# Challenge 2.1 : Update the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use

#########
######### Everything above this line is important setup, not problem-solving.
#########

##### Set up Models #####
## Challenge 2.2: Write models for the tables Movie and Director

class Movie(db.Model):
    __tablename__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(64))
    directorId = db.Column(db.Integer, db.ForeignKey('directors.directorId'))

class Director(db.Model):
    __tablename__ = 'directors'
    directorId = db.Column(db.Integer, primary_key=True)
    directorName = db.Column(db.String(128))

class MovieDirectorForm(FlaskForm):


@app.route("/")
def index():
    form = MovieDirectorForm()
    return render_template("index.html", form=form)

@app.route("/addMovie")
    pass

@app.route("/viewMoviews")
    pass

if __name__=='__main__':
    app.run()
