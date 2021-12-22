#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
<<<<<<< HEAD
from models import storage
from models.engine import DBStorage

=======
import models
>>>>>>> 5acefeff6f2412feb2e53df9529a97b8601146dd

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
