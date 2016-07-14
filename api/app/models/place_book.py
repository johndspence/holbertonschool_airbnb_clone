import base
import user
from base import *
from app.models.amenity import *
from app.models.city import *
from app.models.place_amenity import *
from app.models.user import *

'''
Creates class Place_Book which is used to for creation and interaction with
the mysql database
'''

class PlaceBook(BaseModel):
	place = ForeignKeyField(Place)
	user = ForeignKeyField(User, related_name = 'places_booked')
	is_validated = BooleanField(default = False)
	date_start = DateTimeField(null = False)
	number_nights = IntegerField(default = 1)

	def to_hash(self):
		return {'id':self.id, 'created at': self.created_at, 'updated_at':
		self.updated_at, 'place_id': self.place_id, 'user_id': self.user_id,
		'is_validated': self.is_validated, 'date_start': self.date_start,
		'number_nights': self.number_nights}
