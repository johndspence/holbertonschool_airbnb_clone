from flask import Flask
from flask_json import FlaskJSON
import app
import config

from app import app
from app.views import *

if __name__ == '__main__':
	app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
