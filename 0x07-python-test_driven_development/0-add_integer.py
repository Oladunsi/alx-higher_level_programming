#!/usr/bin/python3

"""
created on Feb 1 2023 1:18AM
@Author: Oke Oladunsi Samuel
"""


def add_integer(a, b=98):
    """A function summing up two integers
      args:
          a (int): An integer
          b (int): An integer
      raises:
           TypeError: if either a or b not an integer
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("a must be an integer")
    return int(a) + int(b)
