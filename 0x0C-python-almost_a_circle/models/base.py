#!/usr/bin/python3

# Author: Oke Oladunsi Samuel
# Created on 2/11/23

"""A class that manage id attribute in all your future 
        classes and to avoid duplicating the same code"""

class Base:
    """ The base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializing the base class
        Args:
            id (int): represent the amount of instances made
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


