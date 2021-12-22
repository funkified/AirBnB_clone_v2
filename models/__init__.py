#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place

if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
