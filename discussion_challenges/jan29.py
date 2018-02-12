from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import Required

import requests
import json

api_key = "f2ee269209adf68243f81d4d35db7fb4"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lollstr'

class WeatherForm(FlaskForm):
	zip_code = IntegerField("Enter your zip code: ", validators=[Required()])
	submit = SubmitField()

	def validate_zipcode(self, field):
		if len(field) != 5:
			raise ValidationError("Not a valid zipcode!")

@app.route("/zipcode", methods = ["GET", "POST"])
def form():
	form_var = WeatherForm()
	return render_template("zipform.html", form=form_var)
def zip():
	form = WeatherForm(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		z = form.zip_code.data
		return render_template('resultz.html', zip_code=z)
	flash('All fields are required!')
	return redirect(url_for('form'))




if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
