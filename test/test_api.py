from flask import Flask 
import pytest
import requests
import json


#test 1: verify correct HTTP status code - by executing an API call with valid required params; should return 2XX code
									#	 - maybe attempt to use a city with two words and attempt to use a city and state that are the same (ie. new york, new york)

def test_status_code_201():
	"""test with valid input"""
	city = "Boston"
	state = "MA"
	
	state = state.lower()
	city = city.lower()
	ocdState = "ocd-division/country:us/state:"+ state
	ocdPlace = ocdState + "/place:" + city
	
	Ids=[ocdState, ocdPlace]
	
	params={'district-divisions': ','.join(Ids)}
	
	headers = {"Accept": "application/json"}
	url = 'https://api.turbovote.org/elections/upcoming?'

	"""using the requests module the OCD-IDs are added to the URL as the query string and the request is made on the API"""
	r = requests.get(url, params=params, headers=headers)
	#validating the status code
	assert r.status_code == 200
	
	
	

	

	


#test 2: verify response params - input invalid params
							#   - input invalid value for param (ie. city that has numbers, city with hyphen?)
							#	- input empty param (ie no city or no state)
#test 3: verify response headers??
#test 4: verify correct application state - for GET requests, verify that there is no state change in the system

#test 5: verify basic performance sanity - response is received in a timely manner 




