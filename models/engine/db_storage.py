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

    """ def all(sel, cls=None):
        self.__engine.query() """
