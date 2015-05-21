from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
#from flask_debugtoolbar import DebugToolbarExtension
from secrets import amm_chain



app = Flask(__name__)

app.secret_key = "abc123"

app.jinja_env.undefined = StrictUndefined

amm_search_url= 'https://api.ammado.com/v1/search?apiKey='+amm_chain

@app.route('/')
def index():


	return render_template("homepage.html")


@app.route("/login", methods=['GET'])
def login():


	return render_template("login.html")


@app.route("/login_submit", methods=['POST'])
def login_submit():


	return render_template("login_submit.html")


@app.route("/signin", methods=['POST'])
def signin():


	return render_template("signin.html")

@app.route("/search", methods=['GET'])
def search():
	if request.method== "GET":		
		return render_template("search.html")

	else:
		keyword= request.form.get('select_form')
		
		#if submitting form, go to API to do search
		search= request.get(amm_search_url+'&keyword='+keyword)

		return render_template('results.html', search=search.text)

@app.route("/donate", methods=['POST'])
def donate():


	render_template("donate.html")

if __name__ == '__main__':


	app.debug = True

	#DebugToolbarExtension(app)

	app.run()