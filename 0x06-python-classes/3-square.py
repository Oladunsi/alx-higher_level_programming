#!/usr/bin/python3
"""
Created on Wed Jan 25 5:14 2023
@author: Oke Oladunsi Samuel
"""


class Square:
    """A square class representation"""
    def __init__(self, size=0):
        """Initializing the square
        Args:
            size (int): size of the new square
        Errors:
            TypeError: When size not an integer
            ValueError: When size less zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square based on the size"""
        return self.__size * self.__size
