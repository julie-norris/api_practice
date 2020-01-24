from flask import Flask, request, render_template, session, redirect 
import requests, json
from us_states import postal_abbreviations



app=Flask(__name__)



@app.route('/')
def index():
	"""Homepage"""

	return render_template("address_form.html", states=postal_abbreviations)



"""When the user submits the form, your code will translate the address into some OCD-IDs"""


@app.route('/search', methods=['POST'])
def translate_user_address():
	"""Translates the address submitted into OCD-IDs"""

	"""setting information submitted from user to variable names"""
	city = request.form["city"]
	state = request.form["state"]
	
	
	"""translate the address into some OCD-IDs"""
	state=state.lower()
	city=city.lower()
	ocdState="ocd-division/country:us/state:"+ state
	ocdPlace= ocdState + "/place:" + city
	

	"""Query the Democracy Works Elections API for upcoming elections for those OCD-IDs"""
	Ids=[ocdState, ocdPlace]
	
	params={'district-divisions': ','.join(Ids)}
	
	headers = {"Accept": "application/json"}
	url = 'https://api.turbovote.org/elections/upcoming?'
	r = requests.get(url, params=params, headers=headers)
	r=r.text
	if r == None:
		return ("No upcoming elections near you!")
	else:
		rslt=json.loads(r)

	"""Returned elections are displayed to the user
	The results are formatted for the user"""

	return render_template("election_results.html", rslt=rslt)



if __name__ == '__main__':
	app.run(debug=True)