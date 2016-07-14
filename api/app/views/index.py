
from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

from app import app
from peewee import *

@app.route('/', methods=['GET'])
@as_json
def index():

	utc = datetime.utcnow()
	now = datetime.now()
	return json_response(time=utc,now=now)

def before_request():
	database.connect()

def after_request():
	database.close()

def not_found():
	return json_response(code=404,msg='not found')
