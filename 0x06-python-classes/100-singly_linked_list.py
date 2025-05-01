#!/usr/bin/python3
"""A module that creates a singly linked list"""


class Node:
    def __init__(self, data, next_node=None):
        """initializing Node attributes
        Args:
            data: the data of a node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data attributes"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data attribute, ensuring it's an integer"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next_node attribute"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node attribute, ensuring its a Node or None"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next node must be a Node object")
        self.__next_node = value


"""Defines a singly linked list"""


class SinglyLinkedList:
    def __init__(self):
        """creates an empty singly linked list"""
        self.head = None

    def __str__(self):
        """make list printable"""

        printll = ""
        temp = self.head
        while temp:
            printll += str(temp.data) + "\n"
            temp = temp.next_node
        return printll[:-1]

    def sorted_insert(self, value):
        """inserts node in a sorted way
        Args:
            value: the data of each node
        """
        new_node = Node(value)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        while temp.next_node is not None:
            if new_node.data < temp.next_node.data:
                new_node.next_node = temp.next_node
                temp.next_node = new_node
                return
            else:
                temp = temp.next_node
        temp.next_node = new_node
