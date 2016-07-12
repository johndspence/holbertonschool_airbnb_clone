from flask import Flask, jsonify, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

from app import app


@app.route('/', methods=['GET'])
@as_json
def index():
	'''return flask.jsonify(app)'''
	return { 'TEST' : 12 }

'''
def before_request()

def after_request()

def not_found()
'''
