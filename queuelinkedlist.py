from abc import ABC, abstractmethod

#A class that creats a node for a linked list
class SinglyLinkedListNode:
    #Constructor
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    #Getter & setter methods

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_next_node(self):
        return self._next_node

    def set_next_node(self, new_next_node):
        self._next_node = new_next_node

    #A method for a string representation of the class
    def __str__(self):
        return (str(self._data))

#A class that creats a linked list of nodes
class SinglyLinkedList:
    #Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Getter and setter methods

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_size(self):
        return self.size

    #A method add a new node at the beginning of the list
    def add_node_beginning_of_list(self, data):
        #Creates new node
        new_node = SinglyLinkedListNode(data, None)
        
        #Checks if head already exists
        if self.head:
            temp = self.head
            self.head = new_node

            self.head.set_next_node(temp) 
        #Otherwise, our new node will be assigned to head
        else:
            self.head = new_node
            self.tail = new_node
        
        #Increments size of singly linked list
        self.size += 1
        
    #A method add a new node at the end of the list
    def add_node_end_of_list(self, data):
        #Creates a new node
        new_node = SinglyLinkedListNode(data, None)

        #Checks if tail already exists
        if self.tail:
            temp = self.tail
            self.tail = new_node

            temp.set_next_node(self.tail)
        #Otherwise, our new node will be assigned to head & tail
        else:
            self.head = new_node
            self.tail = new_node
        
        #Increments size of singly linked list
        self.size += 1

    #A method remove the node at the beginning of the list
    def remove_node_at_beginning_of_list(self):
        #Removes head when the list has more than 1 node
        if self.head and self.size > 1:
            temp = self.head
            self.head = self.head.get_next_node()

            temp.set_next_node(None)
            self.size -= 1

            return temp
        
        #Removes head when list has only 1 node
        elif self.head and self.size == 1:
            temp = SinglyLinkedListNode(self.head.get_data(), None)
            self.head = None

            self.size -= 1

            return temp
        
        #If list is empty then we just return
        else:
            return
    
    #A method remove the node at the beginning end the list
    def remove_node_at_end_of_list(self):
        #Removes tail when the list has more than 1 node
        if self.tail and self.size > 1:
            #A while loop that finds the node before tail
            index = 1
            curr = self.head
            while(index < self.size):
                curr = curr.get_next_node()
                
                index += 1
            
            self.tail = curr
            curr.set_next_node(None)

            self.size -= 1

            return curr
        
        #Removes tail when list has only 1 node
        elif self.tail and self.size == 1:
            temp = SinglyLinkedListNode(self.tail.get_data(), None)
            self.tail = None

            self.size -= 1

            return temp
        
        #If list is empty then we just return
        else:
            return

    #A method to find return the size of the list
    def __len__(self):
        return self.size

    #A method that traverses and prints each element from the list
    def print_list(self):
        #Sets index to 0 and assigns the current node to head
        index = 1
        curr = self.head

        while(index <= self.size):
            #Prints current node
            print('\nNode num: ' + str(index))
            print(str(curr))

            if curr.get_next_node() is not None:
                #Points to the next node for the next loop
                curr = curr.get_next_node()
            
            index += 1

'''An Abrasct class that offers methods for a queue class'''
class AbstractQueue(ABC):
    #An abstract method that adds to the back of the queue
    @abstractmethod
    def offer(self, obj):
        pass

    '''An abstract method that removes from the front of the 
        queue and return a reference to the object removed'''
    @abstractmethod
    def poll(self):
        pass

    '''An abstract method that returns reference to the object 
        at the front without removing it from the queue'''
    @abstractmethod
    def peek(self):
        pass

    #An abstract method that returns size of queue
    @abstractmethod
    def __len__(self):
        pass

'''A queue class to implement a queue through the inherit methods 
   from from AbstractQueue'''
class PythonListQueue(AbstractQueue):
    #A constructor to create a list
    def __init__(self):
        self._list = []

    #An implemented method that adds to the back of the queue
    def offer(self, obj):
        self._list.append(obj)

    '''An implemented method that removes from the front of the 
        queue and return a reference to the object removed'''
    def poll(self): 
        return self._list.pop(0)

    '''An implemented method that returns reference to the 
        object at the front without removing it from the queue'''
    def peek(self):
        return self._list[0]

    #An implemented method that returns size of queue
    def __len__(self):
        return len(self._list)

'''A linked list class to implement a queue through the inherit methods 
   from from AbstractQueue'''
class SLLQueue(AbstractQueue):
    #A constructor to create a list
    def __init__(self):
        self._list = SinglyLinkedList()

    #An implemented method that adds to the back of the queue
    def offer(self, obj):
        self._list.add_node_end_of_list(obj)

    '''An implemented method that removes from the front of the 
        queue and return a reference to the object removed'''
    def poll(self):
        return self._list.remove_node_at_beginning_of_list()

    '''An implemented method that returns reference to the object 
        at the front without removing it from the queue'''
    def peek(self):
        return self._list.get_head()

    #An implemented method that returns size of queue
    def __len__(self):
        return self._list.get_size()

#A main class to test the methods from the other clases
class Main:
    print('\n----Testing the PythonListQueue class----')
    
    #Creates queue
    list1 = PythonListQueue()

    #Uses offer method to to add to the queue
    list1.offer(1)
    list1.offer(2)
    list1.offer(3)
    list1.offer(4)
    list1.offer(5)
    list1.offer(6)

    #Displays size of list and peek to look at the first item in queue
    print('\nSize of list1 before: ' + str(list1.__len__()))
    print('\nPeek of first item in queue: ' + str(list1.peek()))

    #A loop to take out and look through each item in the queue
    print('\n__Removing each item in the queue__')

    index = 0
    size = list1.__len__()

    while(index < size):
        print('\n' + str(list1.poll()))
        index += 1

    print('\n----Testing the SLLQueue class----')

    #Creates queue
    list2 = SLLQueue()

    #Uses offer method to to add to the queue
    list2.offer(1)
    list2.offer(2)
    list2.offer(3)
    list2.offer(4)
    list2.offer(5)
    list2.offer(6)

    #Displays size of list and peek to look at the first item in queue
    print('\nSize of list1 before: ' + str(list2.__len__()))
    print('\nPeek of first item in queue: ' + str(list2.peek()))

    #A loop to take out and look through each item in the queue

    print('\n__Removing each item in the queue__')

    index = 0
    size = list2.__len__()

    while(index < size):
        print('\n' + str(list2.poll()))
        index += 1
