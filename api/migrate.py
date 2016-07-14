import app.models.base
from app.models.base import BaseModel
import app
import peewee
from app.models.amenity import *
from app.models.city import *
from app.models.place import *
from app.models.place_amenity import *
from app.models.place_book import *
from app.models.state import *
from app.models.user import *

db.connect()
db.create_tables([Amenity, City, Place, PlaceAmenities, PlaceBook, State, User])
