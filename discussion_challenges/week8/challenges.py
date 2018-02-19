# SI364 DS7
# An application about recording favorite songs & info

import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand # needs: pip/pip3 install flask-migrate

# Configure base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

# Application configurations
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'uyfoylgfyu'

## Task 1: Create a database in postgresql in the code line below, and fill in your app's database URI.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:icedout@localhost:5432/week8"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
manager = Manager(app)
db = SQLAlchemy(app) # For database use
migrate = Migrate(app, db) # This is used for database use/updating. Bear with me, we will cover this in greater detail in lecture.
manager.add_command('db', MigrateCommand) # Add migrate command to manager

#########
######### Everything above this line is important/useful setup, not problem-solving.
#########

##### Set up Models #####
class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    songs = db.relationship('Song',backref='Artist')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),unique=True) # Only unique title songs
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id")) # changed
    genre = db.Column(db.String(64))


##### Set up Forms #####
class SongForm(FlaskForm):
    song = StringField("What is the title of your favorite song?", validators=[Required()])
    artist = StringField("What is the name of the artist who performs it?",validators=[Required()])
    genre = StringField("What is the genre of that song?", validators
        =[Required()])
    submit = SubmitField('Submit')

##### Helper functions
### For database additions / get_or_create functions

def get_or_create_artist(db_session,artist_name):
    # Query the artist table and filter using artist_name
    # If artist exists, return the artist object
    # Else add a new artist to the artist table
    pass

def get_or_create_song(db_session, song_title, song_artist, song_genre):
    # Query the song table using song_title
    # If song exists, return the song object
    # Else add a new song to the song table.
    # NOTE : You will need artist id because that is the foreign key in the song table.
    # So if you are adding a new song, you will have to make a call to get_or_create_artist function using song_artist
    s = Song.query.filter_by(song_title=song).first()
    if s:
        return s
    else:
        s = Song(song=song_title, genre=song_genre, artist=song_artist)
        db_session.add(s)
        db_session.commit()

##### Set up Controllers (view functions) #####

## Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

## Main route
# Task 1.3 : Get the form data and add it to the database.
@app.route('/', methods=['GET', 'POST'])
def index():
    songs = Song.query.all()
    num_songs = len(songs)
    form = SongForm()
    if form.validate_on_submit():
        song=form.song.data
        artist=form.artist.data
        genre=form.genre.data

        s = Song.query.filter_by(song_title=song).first()
        if s:
            flash("You've already saved a song with that title!")
            return redirect(url_for('index'))
        else:
            get_or_create_song(db.session, song, artist, genre)
        ## Get the data from the form
        ## Query the Song table using the song name to check if song exists.
        #####   If song exists, reload the form and flash("You've already saved a song with that title!")
        #####   Else use get_or_create_song function to add the song to the database, and after adding redirect to the /all_songs route.
    return render_template('index.html', form=form,num_songs=num_songs)


# Task 1.4: Update the view function.
## HINTS provided below but I would recommend solving the task without looking at the hints
############################################
############################################
############################################ HINTS ############################################
## 1. Query all songs and assigns the result to variable 'songs'
## 2. Collects the title, artist and genre for each song in a list variable 'all_songs'. You can use a for loop and collect each property in a tuple.
## 3. Use all_songs as a parameter in render_template
############################################
############################################
@app.route('/all_songs')
def see_all():
    return 'Update this view function to view all songs!'

if __name__ == '__main__':
    db.create_all()
    manager.run() # NEW: run with this: python main_app.py runserver
    # Also provides more tools for debugging
