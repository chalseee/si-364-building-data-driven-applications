# Import statements necessary
from flask import Flask, render_template
import requests
import json

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def another_function():
    return 'Hello World!'

@app.route('/user/<yourname>')
def hello_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)

@app.route('/itunes/<artist>')
def hello_artist(artist):
    return '<h1>Hello, {}</h1>'.format(artist)



if __name__ == '__main__':
    app.run()
