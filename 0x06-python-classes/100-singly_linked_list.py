#!/usr/bin/python3
"""class module"""

class Node:
    """define Node class
    
    Node class: >>>>
    attributes: __data type(int)
                __next_node type(Node)
    """
    def __init__(self, data, next_node=None):
        """Constructor
        data: stores data inside node
        next_node: next node in the singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data method"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next_node method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next_node method"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        current_node = self.head
        while current_node:
            string += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return string[:-1]

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next_node and current_node.data < value:
            current_node = current_node.next_node
        if current_node.next_node:
            new_node.next_node = current_node.next_node
        current_node.next_node = new_node
