from base import *
from amenity import *
from place import *
from peewee import *

'''
Creates class PlaceAmenities which is used to for creation and interaction
with the mysql database
'''
class PlaceAmenities(Model):
	place = ForeignKeyField(Place)
	amenity = ForeignKeyField(Amenity)

	class Meta:
		database = db
