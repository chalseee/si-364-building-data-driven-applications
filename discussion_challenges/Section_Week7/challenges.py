import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_script import Shell, Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell


# Configure base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

# Application configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = "uohdiodjoijqdioqeoudh"

# Update the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:icedout@localhost:5432/moviedb"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app) # For database use

#########
######### Everything above this line is important setup, not problem-solving.
#########

##### Set up Forms #####
class MovieDirectorForm(FlaskForm):
    movie_name = StringField('Enter movie name:', validators=[Required()])
    director_name = StringField('Enter director name:', validators=[Required()])
    submit = SubmitField('Submit')

##### Set up Models #####

class Movie(db.Model):
    __tablename__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(64))
    directorId = db.Column(db.Integer, db.ForeignKey('directors.directorId'))


class Director(db.Model):
    __tablename__ = 'directors'
    directorId = db.Column(db.Integer, primary_key=True)
    directorName = db.Column(db.String(128))


##### Set up Models #####
@app.route("/")
def index():
    form = MovieDirectorForm()
    return render_template("index.html", form = form)


@app.route("/addMovie", methods = ["POST", "GET"])
def add_movie():
    #get data from WTForms
    form = MovieDirectorForm()
    if form.validate_on_submit():
        print(form.data)
        director = form.director_name.data
        movie = form.movie_name.data
        d = Director.query.filter_by(directorName=director).first()
        if d:
            print("DIRECTOR EXISTS") #now what if director DOESNT exist?
        else:
            d = Director(directorName=director)
            db.session.add(d)
            db.session.commit()

        m = Movie(movieTitle=movie, directorId=d.directorId)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('view_movies'))
    return render_template('index.html')


@app.route("/viewMovies")
def view_movies():
    movies = Movie.query.all()
    return render_template("view.html", object=movies)


if __name__=='__main__':
    db.create_all()
    manager.run()
    app.run(debug = True, use_reloader=True)
