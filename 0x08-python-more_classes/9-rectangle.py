#!/usr/bin/python3


"""
Created on Jan 31 2023
@Author: Oke Oladunsi Samuel
"""


class Rectangle:
    """A rectangle representation in python"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This Initialize a rectangle class
        Args:
            width (int): an integer
            height (int): an integer
        Returns:
               Nothing
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = "#"

    @property
    def width(self):
        """property function to get rectangle width"""
        return self.__width

    @property
    def height(self):
        """property function to get rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter width sets the value for the rectangle width

        args:
           value (int): an integer corresponding to rect width
        Raises:
             ValueError: if value is less than zero (0)
             TypeError: if value is not an integer
             """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("if value is not an integer")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter height sets the value for the corresponding rectangle height
        args:
             value (int): an integer corresponding to rect height
        Raises:
            ValueError: if value is less than zero
            TypeError: if value is not an instance of int
       """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("if value is not an integer")
        else:
            self.__height = value

    def area(self):
        """method to determine rectangle area
        args:
            None
        Returns:
            self.__width * self.__height
        """
        return self.__width * self.__height

    def perimeter(self):
        """method to determine the perimeter of the rectangle
        args:
            None
        Returns:
            p = 2 * (width + height)
            """
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """method to print rectangle
        Returns:
            prints a rectangle of # characters
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self) -> str:
        """A method __repr__ method for object rectangle
        Return:+
            string (str): string to get
        """
        return "Rectangle( {}, {})".format(self.__width, self.__height)

    def __del__(self):
        """a method to detect instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect1,  rect2):
        """Return the Rectangle with the greater area
        args:
            rect1: an instance of class Rectangle
            rect2: an instance of class Rectangle
        Raise:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect1.area() > rect2.area():
            return rect1
        return rect2

    @classmethod
    def square(cls, size=0):
        """
        Class method that defines a square

        args:
            cls: this argument points to class
            size : points to both width and height
            size = width = height
        """
        return cls(size, size)
