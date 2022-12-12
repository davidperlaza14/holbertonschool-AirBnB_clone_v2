#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.environ['HBNB_TYPE_STORAGE']

class State(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ The State  class """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'states'
        name= Column(String(128), nullable=False)
        cities = relationship("City", bockref="state", coscode="delete")
    else:
        name = ""

        @property
        def cities(self):
            from models.city import City
            from models import storage

            city_objects =storage.all(City)
            return [city for city in city_objects.values() if city.state_id == self.id]