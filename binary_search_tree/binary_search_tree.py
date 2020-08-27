"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
                return
            self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
                return
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        root = self
        if root != None:
            is_found = self._find(target, root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, target, curr_node):
        if target > curr_node.value and curr_node.right:
            return self._find(target,curr_node.right)
        elif target < curr_node.value and curr_node.left:
            return self._find(target, curr_node.left)
        if target == curr_node.value:
            return True



    # Return the maximum value found in the tree
    def get_max(self):
        root = self
        list_of_values = self._preorder_traveral(root, [])
        print(list_of_values);
        return max(list_of_values)

    def _preorder_traveral(self, start, traversal):
        if start != None:
            traversal.append(start.value)
            traversal = self._preorder_traveral(start.left, traversal)
            traversal = self._preorder_traveral(start.right, traversal)
        return traversal


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        root = self
        list_of_values = self._preorder_traveral(root, [])
        for i in range(0,len(list_of_values)):
            list_of_values[i] = fn(list_of_values[i])
        return list_of_values

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        from collections import deque

        queue = deque()

        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            print(current.value)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()

            print(current.value)
            
            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

    def in_order_dft(self):
        pass




"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.get_max()

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
