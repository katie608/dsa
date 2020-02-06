"""
Implementation of Doubly Linked List
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
            new.next = self.index(i).next
            new.next.prev = new
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
                print("index value: ",self.index(i).val, ", ", self.index(j).val)
                sum += self.index(i).val*self.index(j).val
        return sum



llone = DLL()

# llone.insert(b, 1)
llone.push(Node(1))
llone.push(Node(2))
llone.push(Node(3))


# llone.insert(Node(10), 1)


print("length: ",llone.length)
print("head value: ", llone.head.val)
print("head.prev: ", llone.head.prev)
print("head.next: ", llone.head.next)
print("tail value: ", llone.tail.val)
print("tail.prev: ", llone.tail.prev)
print("tail.next: ", llone.tail.next)

print("\n \n")
for i in range(llone.length):
    print("List value ", i, " is ", llone.index(i).val)
    print("List prev ", i, " is ", llone.index(i).prev)
    print("List next ", i, " is ", llone.index(i).next)
    print("\n")

print("multiplyAllPairs: ", llone.multiplyAllPairs())

# print("result of multiplyAllPairs: ", llone.multiplyAllPairs())

import pytest

def test_function():
    assert llone.index(2).val == 3, "push() test failed"



# test_function()
