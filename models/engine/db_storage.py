#!/usr/bin/python3
"""This is the db_storage class for AirBnB"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place

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

        session = Session(bind=self.__engine)

    def all(sel, cls=None):
        new_dic = {}
        our_class = eval(cls)
        if cls is not None:
            for param in self.__session.query(our_class):
                new_dic[cls + "." + param.id] = param
            return new_dic
        else:
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
        Base.metadata.create_all(self.__engine)
        our_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(our_session)
        self.__session = Session()
