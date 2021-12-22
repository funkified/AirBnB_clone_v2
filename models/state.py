#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City

import models

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
