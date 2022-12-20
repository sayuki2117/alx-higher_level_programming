#!/usr/bin/python3
# 2-square'py
# @sayuki2117

"""Square class Defination"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
