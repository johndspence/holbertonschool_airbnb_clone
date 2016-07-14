import peewee
import os
import json
import datetime
from config import *

'''
Creates the Peewee MySQL variable database (with all configuration settings
 from the config.py and based on environment variables)
'''
db = peewee.MySQLDatabase(DATABASE.get("database"),
					host=DATABASE.get("host"),
					port=DATABASE.get("port"),
					user=DATABASE.get("user"),
					passwd=DATABASE.get("password"))

'''Creates the BaseModel for other db tables to inherit from'''
class BaseModel(peewee.Model):
	id = peewee.PrimaryKeyField(primary_key=True, unique=True)
	database = db
	created_at = peewee.DateTimeField\
	(default=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
	updated_at = peewee.DateTimeField\
	(default=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
	'''
	Overloading operator to save updated at prior to built-in save function
	of peewee.Model.
	'''
	def save(self, *args, **kwargs):
		self.updated_at = peewee.DateTimeField\
		(default=datetime.datetime.now.strftime('%Y/%m/%d %H:%M:%S'))
	'''Sets metaclass for instance of BaseModel'''
	class Meta:
		database = db
		order_by = ("id",)
