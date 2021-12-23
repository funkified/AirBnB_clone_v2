#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
