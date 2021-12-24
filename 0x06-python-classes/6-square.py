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
        self.__position = position

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
        if self.size:
            for element in range(self.size):
                print("#" * self.__size)
                print(' ' * self.position[0], end='')
        if self.size == 0:
            print()
            return
        else:
            print("\n" * self.position[1], end='')
    
    @property
    def position(self):
        """get the instance itself: self.__position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """set: __position """
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or value[0] < 0 or \
           type(value[1]) != int or value[1] < 0:
           raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value