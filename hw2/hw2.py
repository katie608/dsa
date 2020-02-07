"""
Implementation of Doubly Linked List
Katie Foster
"""

class Node:
    """
    defines one node of the linked list
    """
    def __init__(self, val):
        """
        val: value of node
        next: pointer to next node of linked list
        """
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    """
    doubly linked list
    """
    def __init__(self):
        """
        head: first node in linked list
        tail: last node in linked list
        length: integer value of number of nodes in the list
        """
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
            if curr == None:
                return None
            curr = curr.next
        return curr
    def push(self, new):
        """ add a new node to the front of the list
        """
        if self.length == 0:
            self.head = new
            self.tail = new
        else:
            if self.length == 1:
                self.tail.prev = new
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.length += 1 # keep track of list length
    def insert(self, new, i):
        """  insert a new node after a given node
        """
        new.prev = self.index(i)
        if self.index(i).next is None:
            self.tail = new
        else:
            new.next = self.index(i+1)
            self.index(i).next = new
            self.index(i+1).prev = new
        self.length += 1 # keep track of list length
    def delete(self, i):
        """ deletes a node at a given index
        """
        before = self.index(i-1)
        after = self.index(i+1)
        if i == 0:
            self.head = after
        else:
            before.next = after
        if i == self.length-1:
            self.tail = before
        else:
            after.prev = before
        self.length -= 1 # keep track of list length
    def multiplyAllPairs(self):
        """ sum over the product of node values for every unique combination
        of different nodes
        """
        sum = 0
        for i in range(self.length):
            for j in range(i+1, self.length):
                sum += self.index(i).val*self.index(j).val
        return sum

"""
Testing
"""

import pytest

def test_function():
    """ tests all functions of DLL
    """
    llone = DLL() # create DLL for testing
    llone.push(Node(1))
    llone.push(Node(2))
    llone.push(Node(3))
    assert llone.length == 3, "length test failed"
    assert(llone.index(0)).val == 3, "push and index test failed"
    assert llone.index(2).val == 1, "push test failed"
    assert llone.multiplyAllPairs() == 11, "multiplyAllPairs test failed"
    llone.insert(Node(10), 1)
    assert llone.index(2).val == 10, "insert test failed"
    llone.delete(2)
    assert llone.index(2).val == 1, "delete test failed"

test_function()


"""
Timing
"""

import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

def make_DLL(n):
    """ creates a doubly linked list with n nodes
    """
    l = DLL()
    for i in range(n):
        # add n nodes to DLL, each with value of i (0, 1, 2, 3, ...)
        l.push(Node(i))
    return l


lltwo = make_DLL(10000)
n = 10000
t = timeit.Timer('lltwo.index(random.randrange(10, 10000))', 'import random',
    globals=locals())
output = t.timeit(50) # times the operation 50 times and averages

def time_index():

    lltwo = make_DLL(10000)
    x_vals = []
    y_vals = []

    for i in range(1000):
        x = random.randint(10, 10000)
        x_vals.append(x)
        t = timeit.Timer('lltwo.index(x)', globals=locals())
        y_vals.append(t.timeit(1))

    plt.scatter(x_vals, y_vals)
    plt.show()
    """this plot shows a slight postive trend with lots of points above the
    rest, which are slightly like outliers, except that there are so many 
    """


def time_multiply():
    lltwo = make_DLL(100)
    x_vals = []
    y_vals = []

    for i in range(500):
        x = random.randint(10, 100)
        x_vals.append(x)
        t = timeit.Timer('lltwo.multiplyAllPairs()', globals=locals())
        y_vals.append(t.timeit(1))

    plt.scatter(x_vals, y_vals)
    plt.show()
    """ there seems to be a slight positive trend but with a couple outliers
    at much lower numbers
    """

time_multiply()


#matplotlib
