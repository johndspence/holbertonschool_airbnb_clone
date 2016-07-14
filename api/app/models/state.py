from base import *
from peewee import *

'''
Creates class State which is used to for creation and interaction with
the mysql database
'''
class State(BaseModel):
	name = CharField(max_length=128, unique = True, null = False)

	def to_hash(self):
		return {'id':self.id, 'created at': self.created_at, \
		'updated_at': self.updated_at, 'name': self.name}
