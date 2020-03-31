#!/usr/bin/python3
"""This is the file storage class for AirBnB"""


class DBStorage:
    """ DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
    """ Instantiation of DBStorage class"""
    self.__engine = create engine()
