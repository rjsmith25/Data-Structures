"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value);
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if list is empty, do nothing
        if not self.head:
            return
        # if list only has one element set head and tail to none
        if self.head.next == None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        # remove element from head
        head_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return head_value
    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new Node
        new_node = ListNode(value)
        # check if list is empty
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head == None and self.tail == None:
            return

        # if only 1 element
        if self.head.next == None:
            node_value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return node_value

        node_value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return node_value
    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):

        # if node is at head
        if self.head.value == node.value:
            self.remove_from_head()
            return

        # if node is at the tail
        if self.tail.value == node.value:
            self.remove_from_tail()
            return

        # start at the head and find current spot and just remove
        current_node = self.head

        while current_node.value != node.value:
            current_node = current_node.next

        previous_node = current_node.prev
        previous_node.next = current_node.next
        current_node.next.prev = previous_node

        current_node.next = None
        current_node.prev = None
        current_node = None

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
        # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max
