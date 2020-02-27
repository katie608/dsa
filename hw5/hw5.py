"""
Implementation of a Minimum Heap
"""

import pytest
from hypothesis import given
import hypothesis.strategies as st

import math

class Heap:
    """
    Implement a min-heap that supports the following operations with the given
    runtime in parantheses
    """
    def __init__(self, oglist=[]):
        """
        given a (possibly empty) list of elements initialize a heap in-place
        (O(n))
        """
        self.list = oglist

        if len(oglist) < 1:
            self.root = None
            print("Input list is empty")
        else:
            self.root = oglist[0]

        for i in range(len(self.list)-1, -1, -1):
            self.sort_heap(i)

    def getParent(self, index):
        """returns index of parent"""
        i = (index-1)//2
        if i < 0:
            return None
        return i

    def getLchild(self, index):
        """returns index of left child"""
        i = 2*index + 1
        if i > len(self.list)-1:
            return None
        return i

    def getRchild(self, index):
        """returns index of right child"""
        i = 2*index + 2
        if i > len(self.list)-1:
            return None
        return i

    def sort_heap(self, parent):
        """
        Sorts heap, takes in index of parent
        (O(n))
        """
        Lchild = self.getLchild(parent)
        Rchild = self.getRchild(parent)
        elms = self.list

        if Lchild!=None and Rchild!=None: # checks that both children exist
            # swap with smaller child if child is smaller than parent
            if elms[parent] < elms[Lchild] and elms[parent] < elms[Rchild]:
                # if parent < than both children, return
                return
            elif elms[Lchild] <= elms[Rchild]:
                # if Lchild <= Rchild, swap parent with Lchild
                temp = elms[Lchild]
                elms[Lchild] = elms[parent]
                elms[parent] = temp
                self.sort_heap(Lchild)
            else:
                # swap parent with Rchild
                temp = elms[Rchild]
                elms[Rchild] = elms[parent]
                elms[parent] = temp
                self.sort_heap(Rchild)

        elif Lchild != None and elms[Lchild] <= elms[parent]:
            # if Lchild is only child and Lchild<parent, swap parent with Lchild
            temp = elms[Lchild]
            elms[Lchild] = elms[parent]
            elms[parent] = temp
        else:
            # if both children are missing, return/exit
            return

    def length(self):
        """
        return the number of elements in the heap
        (O(1))
        """
        return len(self.list)

    def insert(self, value):
        """
        insert a new element into the heap
        (O(log n))
        Put it in last element of list and do something like
        the opposite of sort heap (look at parent, swap with parent if needed
        until you don't need to swap with parent), switch index and recurse
        """
        self.list.append(value) # add new item to end of list
        curr = len(self.list)-1 # set curr to item that was just appended
        parent = self.getParent(curr) # get index of parent of curr

        while self.list[curr] < self.list[parent]:
            temp = self.list[curr]
            self.list[curr] = self.list[parent]
            self.list[parent] = temp
            if parent>0:
                curr = parent
                parent = self.getParent(curr)
            else:
                return


    def find_min(self):
        """
        return the minimum value (root) in the heap
        (O(1))
        """
        return self.list[0]

    def delete_min(self):
        """
        delete the minimum value element in the heap
        (O(log n))
        swap first and last element in list, delete new last element
        Then swap using sort_heap with index 0
        """
        # put copy of last item of list at top, overwriting min
        self.list[0] = self.list[len(self.list)-1]

        # delete last item of list
        self.list.pop()

        # sort heap starting at top, which sends element down
        self.sort_heap(0)

    def sorted_list(self):
        """
        returns a new list containing all the elements from min to max
        (O(n log n))
        break down the tree from above
        make a copy of the heap so you can modify the copy
        return the min (add it to the list)
        then delete the min
        then sort the list
        """
        if self.list == []:
            return None
        copy = self
        sorted = []
        # continuously return the min, add min to sorted[], then delete min
        for i in range(len(copy.list)):
            sorted.append(copy.list[0])
            copy.delete_min()
        return sorted

    def display_heap(self):
        """
        prints heap in a friendly manner
        """
        if len(self.list)<=0:
            return
        print("\n")
        # finds height and width of the heap tree
        width = 2**math.floor(math.log2(len(self.list)))
        height = math.floor(math.log2(len(self.list))) + 1

        id = 0 # indexing variable
        for i in range(height): # iterates over each row
            edge_spaces = 2**(height-i-1)-1 # calculates spaces on edge
            in_spaces = 2**(height-i)-1 # calculates spaces between elements
            mid_text = "" # initializes empty string for middle text
            for j in range(2**i): # iterates through all elements on a row
                mid_text+= str(self.list[id])
                mid_text+= in_spaces*" "
                id+=1
                if id==len(self.list):
                    print(" "*edge_spaces, mid_text, "\n")
                    return
            print(" "*edge_spaces, mid_text, "\n")


l = [9, 4, 1, 9]
import random
l2 = [5, 6, 7, 5, 6, 3, 4, 5, 4, 4]

l2 = []
print("Original list: ", l2)

h = Heap(l2)
print("Heap: ", h.list)
h.display_heap()
# print(h.sorted_list())
# h.delete_min()
# h.insert(3)
# print("After insert: ", h.list)
# h.display_heap()

print(min(l2), h.return_min())


""" Hypothesis """
import pytest
from hypothesis import given
import hypothesis.strategies as st

@given(st.lists(st.integers())) # gives you a random list of integers
def test_heap_len(l):
    h = Heap(l) # make random list of integers into a heap
    print(len(l), h.length())
    assert len(l) == h.length()

@given(st.lists(st.integers()))
def test_heap_add_delete_min(l):
    """
    test sequentially inserting integers into a
    heap and then sequentially deleting the minimum until the heap is empty.
    """
    h = Heap([])
    for i in range(len(l)):
        h.insert(l[i])
    print(min(l), h.find_min())
    assert min(l) == h.find_min()
    for i in range(len(l)):
        h.delete_min()
    assert h.list == []

@given(st.lists(st.integers()))
def test_heap_init_delete(l):
    """
    test initializing a heap with a list and then
    sequentially deleting the minimum until the heap is empty
    """
    h = Heap(l)
    for i in range(len(l)):
        h.delete_min()
    assert h.list == []

@given(st.lists(st.integers()))
def test_heap_sort(l):
    """
    test initializing a heap with a list and then
    returning a sorted version of that list.
    """
    h = Heap(l)
    print(l.sort(), h.sorted_list())
    assert l.sort() == h.sorted_list()
