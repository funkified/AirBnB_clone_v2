#!/usr/bin/python3
"""
Module: DB_Storage
Database engine to manage data
"""


from os import getenv
from models.base_model import BaseModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from os import getenv

class DBStorage():
    """
    """
    __engine = None
    __session = None
    """
    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City
                }
    """
    def __init__(self):
        """"""""
        User = getenv('HBNB_MYSQL_USER')
        Password = getenv('HBNB_MYSQL_PWD')
        Host = getenv('HBNB_MYSQL_HOST')
        Database = getenv('HBNB_MYSQL_DB')
        Env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb:// {}: {}@{}:3306/{}'.format(
                                      User, Password, Host, Database),
                                      pool_pre_ping=True)

        if Env == 'test':
            """ Drop all tables """
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        dict_cls = {}

        if cls:
            for obj in self.__session.query(cls).all():
                if obj.__class__.__name == cls.__name__:
                    dict_cls[k] = obj
            return dict_cls
        else:
            return DB_Storage.__objects

    def new(self, obj):
        """
        add the object to current database session
        """
        if obj:
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
