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

	# if 'keyword' in request.args:
		
	# 	keyword = request.args['keyword']
	# 	#if submitting form, go to API to do search
	# 	search= requests.get(amm_search_url+'&keyword='+keyword)
	# 	# pprint.pprint(search.json())
	# 	results = search.json()['results']
	# 	pprint.pprint(results)

	# 	filtered_results = []		
	# 	for key in results:
	# 		print results[key]['beneficiaryName']
	# 		print results[key]['beneficiaryId']
	# 		print results[key]['strapline']
	# 		if 'country' in results[key]:
	# 			if results[key]['country'] == 'US':
	# 				print results[key]['country']
	# 		print results[key]['beneficiaryType']
	# 		filtered_results.append(results[key])

	# 	pprint.pprint(filtered_results)

	# 	return render_template('results.html', results=filtered_results)


		#make a dictionary of {beneficiary name: benefic_id, ... }
		#iterate through list, add to my dictionary

		# beneficiaryName = request.args["beneficiaryName"]
		# beneficiaryId = request.args["beneficiaryId"]
		# strapline = request.args["strapline"]
		# country = request.args["country"]
		# beneficiaryType = request.args["beneficiaryType"]
		

	# search_info = {'beneficiaryName' : 'beneficiaryId', 
	# 					'strapline' : [],
	#                     'country' : "US",
	# 					'beneficiaryType' : 'nonprofit'}

	# for keyword in search_info:


	#my_dict = {}
		
	#for keyword in search_info:
  	#		my_dict.append(keyword)


  	#		return my_dict
  	# print search_info

	return render_template("search.html")

  	# for k in search.iteritems():


			# return render_template('results.html', search=search.json(),
			# 								   beneficiaryName=beneficiaryName,
			# 							       strapline=strapline,
			# 							       country=country,
			# 							       beneficiaryType=beneficiaryType
			# 							       )
			# print "Search results are:"('%s, %s, %s, %s,') % (search[beneficiaryName], [strapline],
			# [country], [beneficiaryType])

	
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
			print str(results[key]['beneficiaryName'])
			print str(results[key]['beneficiaryId'])
			print str(results[key]['strapline'])
			if 'country' in results[key]:
				if results[key]['country'] == 'US':
					print str(results[key]['country'])
			if results[key]['beneficiaryType'] == 'nonprofit':
				print str(results[key]['beneficiaryType'])
			filtered_results.append(results[key])

		# pprint.pprint(filtered_results)

		return render_template('results.html', results=filtered_results)


@app.route("/donate", methods=['GET'])
def donate():


	return render_template("donate.html")

if __name__ == '__main__':


	app.debug = True

	#DebugToolbarExtension(app)

	app.run()