#!/usr/bin/python3

"""Define square class. """


class Square:
    """ Square Reprentation. """

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): size of new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate Square Area.

        Args:
            area (int): the area of a square

        Return:
            int: the area of the square
        """

        self.area = self.__size ** 2
        return (self.area)
