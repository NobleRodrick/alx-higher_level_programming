#!/usr/bin/python3
"""Definition of the square class"""


class Square:
    """Body of the class"""

    def __init__(self, size=0):
        """class constructor.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """return new size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)
