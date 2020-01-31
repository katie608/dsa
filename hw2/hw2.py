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
    def __init__(self, head, tail, length):
        """
        head: first node in linked list
        tail: last node in linked list
        length: integer value of number of nodes in the list
        """
        self.head = head
        self.tail = tail
        self.length = length
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
    def push(self, new):
        """ add a new node to the front of the list
        """
        new.next = self.head
        self.head = new
        self.length += 1 # keep track of list length
    def insert(self, new, i):
        """  insert a new node after a given node
        not sure if I accounted for all cases here
        eg: if end of list, set to tail, if beginning, set to head
        """
        new.next = self.index(i)
        self.index(i-1).next = new
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
                sum += self.index(i).val*self.index(j).val
        return sum


d = Node(20, None)
c = Node(16, None)
b = Node(14, c)
a = Node(12, b)

ll = SLL(a, c, 2)

# ll.push(a)
ll.push(d)
# ll.push(c)

print(ll.index(3).val)
print(ll.multiplyAllPairs())
