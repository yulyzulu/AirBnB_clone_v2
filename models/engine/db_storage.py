#!/usr/bin/python3
"""This is the db_storage class for AirBnB"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
import os


class DBStorage:
    """ DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class"""
        var_env = os.getenv("HBNB_ENV")
        sql_user = os.getenv("HBNB_MYSQL_USER")
        sql_passwd = os.getenv("HBNB_MYSQL_PWD")
        sql_host = os.getenv("HBNB_MYSQL_HOST")
        sql_db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb:\
//{}:{}@{}:3306/{}".format(sql_user, sql_passwd, sql_host, sql_db),
            pool_pre_ping=True)

        if var_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = [State, City, User, Place, Review, Amenity]
        new_dic = {}
        if cls is not None:
            our_class = eval(cls)
            for parameter in self.__session.query(our_class):
                del parameter.__dict__['_sa_instance_state']
                new_dic[cls + "." + parameter.id] = parameter
        else:
            for item in classes:
                for i in self.__session.query(item):
                    del i.__dict__['_sa_instance_state']
                    new_dic[item.__class__.__name__ + "." + i.id] = i
        return new_dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            DBStorage.save()

    def reload(self):
        our_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(our_session)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
