from peewee import *
import os
import json
import datetime
from .. import config

'''
Peewee MySQL variable database (with all configuration settings from the right
 config file depending of the environment)
'''
db = MySQLDatabase(config.DATABASE.get("database"),
					host=config.DATABASE.get("host"),
					port=config.DATABASE.get("port"),
					user=config.DATABASE.get("user"),
					passwd=config.DATABASE.get("password"))


class BaseModel(peewee.Model)
