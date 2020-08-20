"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
# Stack class using an array as the underlying storage structure
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size == 0:
#             return
#         element = self.storage.pop(self.size - 1)
#         self.size -= 1
#         return element

# Stack class using linked list as the underlying storage structure
class Node:
    def __init__(self,value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        # create a new Node
        new_node = Node(value)
        # check if list is empty
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self,value):
        # create a new Node
        new_node = Node(value)
        # check if list is empty
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return
        # if list only has one element set head and tail to none
        if self.head.next == None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # more elements
        head_value = self.head.value
        self.head = self.head.next
        return head_value
    def remove_tail(self):
        if self.head == None and self.tail == None:
            return

        if self.head.next == None:
            node_value = self.tail.value
            self.head = None
            self.tail = None
            return node_value

        current = self.head

        while current.next != self.tail:
            current = current.next

        node_value = self.tail.value
        self.tail = current
        current.next = None
        return node_value



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
       if self.size == 0:
           return
       element = self.storage.remove_tail()
       self.size -= 1
       return element
