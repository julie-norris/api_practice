Learn more or give us feedback
from flask import Flask 
from server import app
import pytest
import requests


def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 



