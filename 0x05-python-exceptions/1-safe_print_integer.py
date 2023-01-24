#!/usr/bin/python3

def safe_print_integer(value):
    """A function that print a value using '{:d}'.format(...)

   Args:
         value: expected to be integer
    Return:
          prints value and returns (True) if value is an int
          else - prints nothing and returns (False)
          if value is TypeError or ValueError)
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
