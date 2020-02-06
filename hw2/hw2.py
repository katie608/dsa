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
        # head.next = self.index(1)
        self.tail = None
        # self.tail.prev = self.index(self.length() -1)
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
            new.next = self.head
            self.head = new
            self.head.prev = new
        self.length += 1 # keep track of list length
    def insert(self, new, i):
        """  insert a new node after a given node
        not sure if I accounted for all cases here
        eg: if end of list, set to tail, if beginning, set to head
        """
        new.prev = self.index(i)
        if self.index(i).next is None:
            self.tail = new
        else:
            new.next = self.index(i).next
            new.next.prev = new
            # self.index(i+1).prev = new <-- does same thing as above?
        self.length += 1 # keep track of list length
    def delete(self, i):
        """ deletes a node at a given index
        """
        self.index(i-1).next = self.index(i+1)
        self.length -= 1 # keep track of list length
    def multiplyAllPairs(self):
        """ sum over the product of node values for every unique combination
        of different nodes
        """
        sum = 0
        for i in range(self.length):
            for j in range(i, self.length):
                # print("index value: ",self.index(i).val)
                sum += self.index(i).val*self.index(j).val
        return sum


a = Node(10)
b = Node(11)

# d = Node(13, None)
# c = Node(12, None)
# b = Node(11, c)


llone = DLL()

# llone.insert(b, 1)
llone.push(b)
llone.push(a)

print("length: ",llone.length)
print("head value: ", llone.head.val)
print("head.prev: ", llone.head.prev)
print("head.next: ", llone.head.next)
print("tail value: ", llone.tail.val)
print("tail.prev: ", llone.tail.prev)
print("tail.next: ", llone.tail.next)

# for i in range(llone.length):
    # print("List element ", i, " is ", llone.index(i).val)


# print("result of multiplyAllPairs: ", llone.multiplyAllPairs())

import pytest
def test_function():
    assert llone.index(2).val == 3, "push() test failed"



# test_function()
