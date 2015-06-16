from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session

from secrets import amm_chain, all_chain
import pprint

import requests

import json


from model import User, Nonprofit, connect_to_db, db

from flask.ext.login import LoginManager
from flask.ext.login import login_user, login_required, current_user

from datetime import datetime


app = Flask(__name__)
app.secret_key = "abc123"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users.login"

amm_search_url= 'https://api.ammado.com/v1/search?apiKey='+amm_chain
all_search_url= 'http://api2.allforgood.org/api/volopps?key='+all_chain

	
@app.route('/')
def index():

	return render_template("homepage.html")



@app.route("/nonprofit_click", methods=['POST'])
def nonprofit_click():

	beneficiaryName = request.form['beneficiaryName']
	categories = request.form['categories'][3:-2]
	beneficiaryId = request.form['beneficiaryId']
	strapline = request.form['strapline']
	country = request.form['country']
	# get permalink
	#if 'permalink' in request.form:
	permalink = request.form['permalink']

	user_id=browser_session["user_id"]
	nonprofit = Nonprofit(beneficiary_name=beneficiaryName, 
		categories=categories,
		beneficiary_id=beneficiaryId,
		strapline=strapline,
		country=country,
		user_id=user_id) 
		
	# store the nonprofit into the database
	db.session.add(nonprofit)
	db.session.commit()

	#redirect to the permalink
	return redirect(permalink)

@app.route("/login", methods=['GET'])
def login():

	if request.args.get('email'):
		session['email'] = request.args.get('email')

	return render_template("login.html")
	
		
	


@app.route("/login", methods=['POST'])
def login_submit():
	email = request.form["email"]
	password = request.form["password"]

	print email
	print password


	user = User.query.filter_by(email=request.form['email']).first()

	if not user:
		flash("We can't seem to locate you. Please try again or Sign In.")
		return redirect("/login")

	if user.password != password:
		flash("Incorrect password. Please try again.")
		return redirect("/login")


	browser_session["user_id"] = user.user_id
	login_user(user)
	flash("%s has been logged in" % email)

	nonprofit_list=Nonprofit.query.filter_by(user_id=user.user_id).all()
	
	print nonprofit_list

	return render_template("login_submit.html")


@app.route("/signup", methods=['GET'])
def signin():


	return render_template("signin.html")


@app.route("/signup", methods=['POST'])
def signin_submit():
	username = request.form["username"]
	email = request.form["email"]
	password = request.form["password"]
	age = int(request.form["age"])
	zipcode = request.form["zipcode"]
	
	user = User(username=username, email=email, password=password, age=age, zipcode=zipcode)
	db.session.add(user)
 	db.session.commit()

 	browser_session["user_id"] = user.user_id
	login_user(user)

 	flash("%s, has been added to the family." % username)
	
	return render_template("login_submit.html", user=user)


@app.route("/search", methods=['GET'])
@login_required
def search():

	

	return render_template("search.html")

@app.route("/results")
def results():

	
	if 'keyword' in request.args:
		
		keyword = request.args['keyword']
		#if submitting form, go to API to do search
		search= requests.get(amm_search_url+'&keyword='+keyword)
		
		results = search.json()['results']
	

		filtered_results = []
		for key in results:
			result= results[key]
			append = True
			if 'currencyCode' in result:
				if result['currencyCode'] != 'USD':
					append = False
			if 'country' in result:
				if result['country'] !='US':
					append = False
			if 'beneficiaryType' in result:
				if result['beneficiaryType'] != 'nonprofit':
					append = False
			if append:
				filtered_results.append(results[key])
			
		user_searches = current_user.nonprofits

		return render_template('results.html', results=filtered_results, user_searches=user_searches)


@app.route("/volunteer", methods=['GET'])
def volunteer():
	
	return render_template("volunteer.html")

@app.route("/volunteer_results")
def volunteer_results():

	if 'category' in request.args:
		if 'zipcode' in request.args:
				
			category = request.args['category']
			zipcode = request.args['zipcode']
			#if submitting form, go to API to do search
			find = requests.get(all_search_url+'&q='+category+'&vol_loc='+zipcode+'&distance=15')
			
			items = find.json()['items']
			
			combo_results = []

			for item in items:
				start = datetime.strptime(item['startDate'], '%Y-%m-%d %X')
				start_time = datetime.strftime(start, '%B %d, %Y %I:%M %p')
				item['startDate'] = start_time
				end = datetime.strptime(item['endDate'], '%Y-%m-%d %X')
				end_time = datetime.strftime(end, '%B %d, %Y %I:%M %p')
				item['endDate'] = end_time
				combo_results.append(item)
				

			return render_template("volunteer_results.html", querys=combo_results)

@app.route('/account_page')
def account_page():

	return render_template("login_submit.html")

@app.route('/logout')
def logout():

	del browser_session["user_id"]
	flash ("Logout successful")

	return redirect("/")


@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)




if __name__ == '__main__':


	app.debug = False

	#DebugToolbarExtension(app)
	connect_to_db(app)


	app.run()