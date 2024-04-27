"""
Carlos Romero

Homework 4: Implement Queue ADT in Python

April 26, 2024
"""

from abc import ABC, abstractmethod


class SinglyLinkedListNode:
    def __init__(self, data):
        self._data = data
        self._next_ptr = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next_ptr(self):
        return self._next_ptr

    def set_next_ptr(self, next_ptr):
        self._next_ptr = next_ptr

    def __str__(self):
        return str(self._data)


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # getters
    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def get_size(self):
        return self._size

    def add_at_beginning_of_list(self, data):
        new_node = SinglyLinkedListNode(data)

        # assign a new node to the head
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        # creating our new node in the beginning of the list
        else:
            new_node.set_next_ptr(self._head)
            self._head = new_node

        self._size += 1

    def add_at_end_of_list(self, data):
        new_node = SinglyLinkedListNode(data)

        # assign a new node to the head & tail
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next_ptr(new_node)
            self._tail = new_node

        self._size += 1

    def remove_at_beginning_of_list(self):
        if self._head is None:
            return
        # if list size is only 1
        elif self._size == 1:
            temp = SinglyLinkedListNode(self._head.get_data()) # might need another parameter
            self._head = None
            self._tail -= 1
            return temp

        # if list size is more than one
        elif self._size > 1:
            temp = self._head
            self._head = self._head.get_next_ptr()

            temp.set_next_ptr(None)
            self._size -= 1
            return temp

    def remove_at_end_of_list(self):
        if self._tail is None:
            return
        elif self._size == 1:
            temp = SinglyLinkedListNode(self._tail.get_data())
            self._tail = None
            self._size -= 1
            return temp

        elif self._size > 1:
            i = 1
            current_node = self._head
            while i < self._size:
                current_node = current_node.get_next_ptr()
                i += 1

            self._tail = current_node
            current_node.set_next_ptr(None)
            self._size -= 1
            return current_node

    def __len__(self):
        return self._size

    def print_list(self):
        list = []
        current = self._head
        while current is not None:
            list.append(str(current.get_data()))
            current = current.get_next_ptr()
        return list


# AbstractQueue: Python abstract classes inherit from the class ABC. Here is an abstract queue class.
class AbstractQueue(ABC):
    # add to the back of the queue
    @abstractmethod
    def offer(self, obj):
        pass

    # remove from the front of the queue and return a reference to the object removed
    @abstractmethod
    def poll(self):
        pass

    # just return a reference to the object at the front without removing it from the queue
    @abstractmethod
    def peek(self):
        pass

    # returns the size of the list
    @abstractmethod
    def __len__(self):
        pass


# PythonListQueue: AbstractQueue implemented with an underlying Python list
class PythonListQueue(AbstractQueue):
    def __init__(self):
        self._list = []

    def offer(self, obj):
        self._list.append(obj)

    def poll(self):
        return self._list.pop(0)

    def peek(self):
        return self._list[0]

    def __len__(self):
        return len(self._list)


# SLLQueue: AbstractQueue implemented with an underlying pythin list being our linked list
class SLLQueue(AbstractQueue):
    def __init__(self):
        self._list = SinglyLinkedList()

    def offer(self, obj):
        self._list.add_at_end_of_list(obj)

    def poll(self):
        return self._list.remove_at_beginning_of_list()

    def peek(self):
        return self._list.get_head()

    def __len__(self):
        return self._list.get_size()


# Not done
class Main:
    my_list = SinglyLinkedList()

    my_list.add_at_beginning_of_list(5)
    my_list.add_at_end_of_list(10)
    my_list.add_at_beginning_of_list(15)
    my_list.add_at_end_of_list(20)
    my_list.add_at_beginning_of_list(20)

    print(my_list.print_list())

