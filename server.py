from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "abc123"

app.jinja_env.undefined = StrictUndefined

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


	return render_template("search.html")



if __name__ == '__main__':


	app.debug = True

	#DebugToolbarExtension(app)

	app.run()