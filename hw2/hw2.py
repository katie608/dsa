"""
Implementation of Singly Linked List
"""

class Node:
    """
    defines one node of the linked list
    """
    def __init__(self, val, next):
        """
        val: value of node
        next: pointer to next node of linked list
        """
        self.val = val
        self.next = next

class SLL:
    """
    singly linked list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def length(self):
        """ returns length of linked list """
        return self.length
    def index(self, i):
        """
        returns a node at a given index in a list
        i is given index
        """
        curr = self.head
        for j in range (i):
            curr = curr.next
        return curr
    def traverse(self):
        """
        """

        pass
    def push(self, new):
        """ add a new node to the front of the list
        """
        new.next = head
        self.head = new
        self.length += 1 # keep track of list length
    def insert(self, new, i):
        """  insert a new node after a given node
        not sure if I accounted for all cases here
        """
        new.next = index(i)
        index(i-1).next = new
    def delete(self, i):
        pass
    def concatenate(self):
        pass
    def multiplyAllPairs(self):
        pass


c = Node(18, None)
b = Node(14, c)
a = Node(12, b)
