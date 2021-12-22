#!/usr/bin/python3
"""
Module: DB_Storage
Database engine to manage data
"""

from os import getenv
from sqlalquemy import create_engine, Metadata
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place


class DBStorage():
    """
    """
    __engine = None
    __session = None

    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
               }

    def __init__(self):
        """"""""
        User = HBNB_MYSQL_USER
        Password = HBNB_MYSQL_PWD
        Host = HBNB_MYSQL_HOST = localhost
        Database = HBNB_MYSQL_DB

        self.__engine = create_engine('mysql+mysqldv:// {}{}:{}/{}'.format(
                                      User, Password, Host, Database),
                                      pool_pre_ping=True)

        if HBNB_ENV == 'test':
            """ Drop all tables """
            Base.metedata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        dict_cls = {}

        if cls:
            for k, v in self.__objects.items():
                if v.__class__.__name == cls.__name__:
                    dict_cls[k] = v
            return dict_cls
        else:
            return DB_Storage.__objects

    def new(self, obj):
        """
        add the object to current database session
        """
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database session and
        current database session from engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self._session = Session()
