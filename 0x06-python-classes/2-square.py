#!/usr/bin/python3

"""
Created on Wed Jan 25 04:36 2023
@author: Oke Oladunsi Samuel
"""


class Square:
    """A class square class representation"""
    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new square
        Errors:
            TypeError: exception with the message size must be an integer
            ValueError: exception with the message size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
