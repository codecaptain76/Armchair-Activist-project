from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
#from flask_debugtoolbar import DebugToolbarExtension
from secrets import amm_chain
import pprint

import requests

import json


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

@app.route("/volunteer_results" methods=['GET'])
def volunteer_results():


return render_template("volunteer_results.html")	
if __name__ == '__main__':


	app.debug = True

	#DebugToolbarExtension(app)

	app.run()