#!/usr/bin/python3
# 2-rectangle.py
# @sayuki2117
""" This is a rectangle class defination file"""


class Rectangle:
    """Representation of a Rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def print(self):
        for el in range(0, self.__height):
            for el_2 in range(0, self.__width):
                print("#", end="")
            print("")
        if self.__width == 0 or self.__height == 0:
            print("")

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            for el in range(0, self.__height):
                for el_2 in range(0, self.__width):
                    s += "#"
                if el != self.__height - 1:
                    s += "\n"
        return s
