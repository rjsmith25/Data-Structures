"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# queue class using an array as the underlying storage structure
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.storage.append(value);
#         self.size += 1;
#
#     def dequeue(self):
#         if self.size == 0:
#             return
#         element = self.storage.pop(0);
#         self.size -= 1;
#         return element;

# queue class using a LinkedList as the underlying storage structure
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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
       if self.size == 0:
           return
       element = self.storage.remove_head()
       self.size -= 1
       return element
