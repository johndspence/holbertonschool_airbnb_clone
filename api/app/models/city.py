from base import *
from state import *
from peewee import *

'''
Creates class City which is used to for creation and interaction with
the mysql database
'''
class City(BaseModel):
	name = CharField(max_length = 128, null = False)
	state = ForeignKeyField(State, related_name = 'cities', \
	on_delete = "CASCADE")

	def to_hash(self):
		return {'id':self.id, 'created at': self.created_at, \
		'updated_at': self.updated_at, 'name': self.name, \
		'state_id': self.state_id}
