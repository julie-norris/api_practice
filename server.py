from flask import Flask, request, render_template, session, redirect 
import requests, json
from us_states import postal_abbreviations



app=Flask(__name__)



"""You are building a web application that can tell people what elections they have coming up based on their address. It is similar to the kinds of things you'd be working on at Democracy Works and uses one of our APIs.



When someone visits the site you create, they will be presented with an address form. """


@app.route('/')
def index():
	"""Homepage"""

	return render_template("address_form.html", states=postal_abbreviations)



"""When the user submits the form, your code will translate the address into some OCD-IDs"""


@app.route('/search', methods=['POST'])
def translate_user_address():
	"""Translates the address submitted into OCD-IDs"""

	"""setting information submitted from user to variable names"""
	street = request.form["street"]
	street2 = request.form["street-2"]
	city = request.form["city"]
	state = request.form["state"]
	zipcode = request.form["zip"]
	
	
	"""translate the address into some OCD-IDs"""
	state=state.lower()
	city=city.lower()
	ocdState="ocd-division/country:us/state:"+ state
	ocdPlace= ocdState + "/place:" + city
	

	"""Query the Democracy Works Elections API for upcoming elections for those OCD-IDs"""
	Ids=[ocdState, ocdPlace]
	
	payload={'district-divisions': ','.join(Ids)}
	
	headers = {"Accept": "application/json"}
	url = 'https://api.turbovote.org/elections/upcoming?'
	r = requests.get(url, params=payload, headers=headers)
	r=r.text
	rslt=json.loads(r)
	print (rslt)
	"""Returned elections are displayed to the user
	The results are formatted for the user"""

	return render_template("election_results.html", rslt=rslt)



if __name__ == '__main__':
	app.run(debug=True)