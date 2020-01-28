from flask import Flask 
import pytest
import requests
import json


def test_status_code_200():
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

def test_status_code_invalid_city():
	"""test with invalid input -- city not exist"""
	city = "anteater"
	state = "NY"
	
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
	assert r.status_code == 400

def test_same_city_and_state():
	"""test with valid input that is an edge case, ie. city and state are the same"""
	city = "NY"
	state = "NY"
	
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
	
	
def test_invalid_inputs():
	"""test with valid input that is an edge case, ie. city and state are the same"""
	city = "3its2wrong"
	state = "NY"
	
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
	assert r.status_code == 400

