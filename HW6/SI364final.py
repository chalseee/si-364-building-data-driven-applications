import os, json, datetime, requests
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from flask_login import LoginManager, login_required, logout_user, login_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

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

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

#Models
#includes 1-many relationship between words and definitions
#includes many-many relationship betweeen words and partofspeech
pos_word = db.Table('pos_word', db.Column('pos_id', db.Integer, db.ForeignKey('partofspeech.id')), db.Column('word_id', db.Integer, db.ForeignKey('words.id')))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Word(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(5))
    word = db.Column(db.String(32))
    phonetic_spelling = db.Column(db.String(32))

class Definition(db.Model):
    __tablename__ = "definitions"
    id = db.Column(db.Integer, primary_key=True)
    definition = db.Column(db.String(264))
    example_sentence = db.Column(db.String(264))
    word_id = db.relationship('Word', backref="Definition")

class PartOfSpeech(db.Model):
    __tablename__ = "partofspeech"
    id = db.Column(db.Integer, primary_key=True)
    part_of_speech = db.Column(db.String(32))

#Form classes will go here
# -->TBD

#View functions - all include the base navigation menu
@app.errorhandler(404)
def page_not_found(e):
    pass #error-handler for a 404 error renders 404.html

@app.errorhandler(500)
def internal_server_error(e):
    pass #error-handler for a 500 error. renders 500.html

@app.route('/login',methods=["GET","POST"])
def login():
    pass #should render a page with a form allowing users to login

@app.route('/logout')
@login_required
def logout():
    pass #should render a page with a form allowing users to logout

@app.route('/register',methods=["GET","POST"])
def register():
    pass #should render a page with a form allowing users to make an account

@app.route('/secret')
@login_required
def secret():
    pass #should render if a user goes on a page that they have to be logged in to use.

@app.route('/', methods=['GET', 'POST'])
def index():
    pass #homepage. should render a login form as well as a menu to view all other pages in app. If submitted correctly, it will take you to the your_words route and flash a success message. otherwise, it will redirect to this page.
        #page doesn't require login.

@app.route('/all_users_words')
def all_words(): #should render a page that shows information about all words that have been added on this app. it will list all information in the words table.
    pass #page doesn't require login.

@login_required
@app.route('/delete/<word_id>')
def delete(): #should allow the user to delete a word from their list of words. this will remove the entry from the words table, but not it's associated definition(s). will submit/route to the your_words page.
    pass #page requires login

@login_required
@app.route('/update/<word_id>')
def update(): #should allow the user to change a word from their list of words and then run a get_or_create fxn to update possible new parts of speech or definition(s). will submit/route to the your_words page.
    pass #page requires login

@login_required
@app.route('/your_words')
def your_words(): #displays all words that the user has added to their collection. also displays a form to enter a word. page will update to show this word in addition to all past ones once the form is submitted correctly. otherwise, it will still redirect to this page, but flash an error message.
    pass #page requires login
    

if __name__ == "__main__":
    db.create_all()
    manager.run()
