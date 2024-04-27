"""
Carlos Romero

Homework 4: Implement Queue ADT in Python

April 26, 2024
"""


class SinglyLinkedListNode:
    def __init__(self, data):
        self._data = data
        self._next_ptr = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next_ptr(self):
        return self

    def set_next_ptr(self, next_ptr):
        self._next_ptr = next_ptr

    def __str__(self):
        return str(self._data)


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

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
        # checks if head already exists
        else:
            temp = self._head
            self._head = new_node
            self._head.set_next_ptr(temp)

        self._size += 1

    def add_at_end_of_list(self, data):
        new_node = SinglyLinkedListNode(data)

        # assign a new node to the head & tail
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        else:
            temp = self._tail
            self._tail = new_node
            self._tail.set_next_ptr(temp)

        self._size += 1

    def remove_at_beginning_of_list(self, data):
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


