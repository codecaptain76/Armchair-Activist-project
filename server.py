from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
#from flask_debugtoolbar import DebugToolbarExtension
from secrets import amm_chain, all_chain
import pprint

import requests

import json
import logging

import getpass

from model import User, connect_to_db, db

from flask.ext.login import LoginManager
from flask.ext.login import login_user



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


@app.route("/login", methods=['GET'])
def login():

	if request.args.get('email'):
		session['email'] = request.args.get('email')

	return render_template("login.html")
	
		
	# email = raw_input("Email:")
	# password = getpass.getpass("Password:")


@app.route("/login", methods=['POST'])
def login_submit():
	email = request.form["email"]
	password = request.form["password"]

	error = None
	# form = LoginForm(request.form)

	# if form.validate_on_submit():
	user = User.query.filter_by(email=request.form['email']).first()

	if not user:
	    flash("We can't seem to locate you. Please try again or Sign In.")
    	return redirect("/login")

	if user.password != password:
		flash("Incorrect password. Please try again.")
        return redirect("/login")


	browser_session["user_id"] = user.id
	login_user(user)
	flash("%s has been logged in" % email)

	return render_template("login_submit.html")


@app.route("/signin", methods=['GET'])
def signin():


	return render_template("signin.html")


@app.route("/signin", methods=['POST'])
def signin_submit():
	username = request.form["username"]
	email = request.form["email"]
	password = request.form["password"]
	age = int(request.form["age"])
	zipcode = request.form["zipcode"]
	
	user = User(username=username, email=email, password=password, age=age, zipcode=zipcode)
	db.session.add(user)
 	db.session.commit()

 	browser_session["user_id"] = user.id
	login_user(user)

 	flash("%s, has been added to the family." % username)
	
	return render_template("login_submit.html", user=user)


@app.route("/search", methods=['GET'])
def search():

	

	return render_template("search.html")


	
@app.route("/results")
def results():

	
	if 'keyword' in request.args:
		
		keyword = request.args['keyword']
		#if submitting form, go to API to do search
		search= requests.get(amm_search_url+'&keyword='+keyword)
		# pprint.pprint(search.json())
		results = search.json()['results']
		# pprint.pprint(results)

		filtered_results = []		
		for key in results:
			if 'currencyCode' in results[key] == 'USD':

				if 'country' in results[key]:
					if results[key]['country'] == 'US':
						print str(results[key]['country'])
					

						if results[key]['beneficiaryType'] == 'nonprofit':
							print str(results[key]['beneficiaryType'])
							print str(results[key]['beneficiaryName'])
							print str(results[key]['beneficiaryId'])
							print str(results[key]['strapline'])

			filtered_results.append(results[key])
			
			if 'country' in filtered_results == '':
		 		if "beneficiaryType" in filtered_results == '':
		 			if 'currencyCode' in filtered_results != 'USD':

							filtered_results.remove(str(results[key]['beneficiaryName']),str(results[key]['beneficiaryId']),
				str(results[key]['strapline']),str(results[key]['country']),str(results[key]['beneficiaryType']))
		# pprint.pprint(filtered_results)
		# for key in filtered_results:
		# 	if 'country' in filtered_results == 'US':
		# 		if 'beneficiaryType' in filtered_results == 'nonprofit':
		# 			print filtered_results

		# 		else:
		# 			if 'country' in filtered_results != 'US':
		# 				if "beneficiaryType" in filtered_results != 'nonprofit':

		# 					filtered_results.remove(results[key]) 

		return render_template('results.html', results=filtered_results)


@app.route("/donate", methods=['GET'])
def donate():


	return render_template("donate.html")

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
				combo_results.append(item)
				

			return render_template("volunteer_results.html", querys=combo_results)

@app.route('/zip_results')
def zipcode_results():
	if 'zipcode' in request.args:

		zipcode = request.args['postalCode']

		retrieve = requests.get(all_search_url+'&vol_loc='+zipcode+'&distance=25&category=&sort=&type=')

		answers = retrieve.json()['answers']
		
		zip_results=[]

		print str(retrieve[key]['title'])
		print str(retrieve[key]['description'])
		print str(retrieve[key]['startDate'])
		print str(retrieve[key]['endDate'])
		print str(retrieve[key]['contactPhone'])
		print str(retrieve[key]['contactName'])
		print str(retrieve[key]['contactEmail'])
		print str(retrieve[key]['locationName'])

		zip_results.append(retrieve[key])	

	return render_template("volunteer_results.html", querys= zip_results)

@app.route('/logout')
def logout():

	del session["user_id"]
	flash ("Logout successful")

	return redirect("/")


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)




if __name__ == '__main__':


	app.debug = True

	#DebugToolbarExtension(app)
	connect_to_db(app)


	app.run()