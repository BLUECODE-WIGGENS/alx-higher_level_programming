#!/usr/bin/python3
"""define square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Only integer on input otherwise raises an
        exception

        size: type(int)
        size: >= 0 otherwise raises exception
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """get the instance itself: self.__size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set: to set size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        method: square area

        Return: the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def position(self):
        """get the instance itself: self.__position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set: __position """
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) == int and type(value[1]) == int and \
           value[1] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
