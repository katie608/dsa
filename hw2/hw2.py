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
        before = self.index(i)
        after = before.next
        new.prev = before
        if before.next is None:
            self.tail = new
        else:
            new.next = after
            before.next = new
            after.prev = new
        self.length += 1 # keep track of list length
    def delete(self, i):
        """ deletes a node at a given index
        """
        before = self.index(i-1)
        after = before.next.next
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
        curr1 = self.head
        curr2 = self.head
        for i in range(self.length):
            curr2 = curr1
            for j in range(i, self.length-1):
                curr2 = curr2.next
                # print(curr1.val, curr2.val)
                sum += curr1.val*curr2.val
            curr1 = curr1.next
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

def make_list(n):
    """ creates a python list with n elements
    """
    l = []
    for i in range(n):
        l.append(i)
    return l

def time_dll_index(l):
    x_vals = []
    y_vals = []

    for i in range(100):
        x = random.randint(10, 10000) # randomly select an x value
        x_vals.append(x)
        t = timeit.Timer('l.index(x)','import random', globals=locals())
        y_vals.append(t.timeit(50))

    plot = plt.scatter(x_vals, y_vals)
    plt.show()


# time_dll_index(make_DLL(10000))

def time_list_index(l):
    x_vals = []
    y_vals = []

    for i in range(1000):
        x = random.randint(10, 10000) # randomly select an x value
        x_vals.append(x)
        t = timeit.Timer('l[x]','import random', globals=locals())
        y_vals.append(t.timeit(50))

    plt.scatter(x_vals, y_vals)
    plt.show()

# time_list_index(make_list(10000))

def time_multiply():
    x_vals = []
    y_vals = []

    for i in range(50):
        x = random.randint(10, 1000) # randomly select an x value
        l = make_DLL(x)
        x_vals.append(x)
        t = timeit.Timer('l.multiplyAllPairs()','import random', globals=locals())
        r = t.timeit(20)
        print(x,", ", r)
        y_vals.append(r)

    plot = plt.scatter(x_vals, y_vals)
    plt.show()


time_multiply()
