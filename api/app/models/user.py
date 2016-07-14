from base import *
from peewee import *
import hashlib

'''Defines a class User for user table of peewee database model'''
class User(BaseModel):
	email = CharField(max_length=128, unique = True, null = False)
	password = CharField(max_length=128, null = False)
	first_name = CharField(max_length=128, null = False)
	last_name = CharField(max_length=128, null = False)
	is_admin = BooleanField(default = False)

 	'''
	Method to convert clear_password in a MD5 string and save it in password
	attribute
	'''
	def set_password(self, clear_password):
		password = hashlib.md5(clear_password)

	def to_hash(self):
		return {'id':self.id, 'created at': self.created_at, \
		'updated_at': self.updated_at, 'email': self.email, \
		'first_name': self.first_name, 'last_name': self.last_name, \
		'is_admin': self.is_admin}
