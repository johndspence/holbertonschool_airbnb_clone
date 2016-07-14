from base import *
from app import *
from peewee import *
from app.models.amenity import *
from app.models.city import *
from app.models.user import *

'''
Creates class Place which is used to for creation and interaction with
the mysql database
'''
class Place(BaseModel):
	owner = ForeignKeyField(User, related_name = 'places')
	city = ForeignKeyField(City, related_name = 'places')
	name = CharField(max_length = 128, null = False)
	description = TextField()
	number_rooms = IntegerField(default = 0)
	number_bathrooms = IntegerField(default = 0)
	max_guest = IntegerField(default = 0)
	price_by_night = IntegerField(default = 0)
	latitude = FloatField()
	longitude = FloatField()

	def to_hash(self):
		return {'id':self.id, 'created at': self.created_at, 'updated_at':
		self.updated_at, 'owner_id': self.owner_id, 'city_id': self.city_id,
		'name': self.name, 'description': self.description,
		'number_rooms': self.number_rooms,
		'number_bathrooms': self.number_bathrooms,
		'max_guest': self.max_guest, 'price_by_night': self.price_by_night,
		'latitude': self.latitude, 'longitude': self.longitude}
