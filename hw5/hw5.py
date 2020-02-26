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
        """Sorts heap, takes in index of parent"""
        Lchild = self.getLchild(parent)
        Rchild = self.getRchild(parent)
        elms = self.list

        if Lchild==None and Rchild==None:
            return # exit

        """
        TODO: change code so I swap with smaller child
        """

        if elms[parent] > elms[Lchild]:
            temp = elms[Lchild]
            elms[Lchild] = elms[parent]
            elms[parent] = temp
            self.sort_heap(Lchild)


        if Rchild != None and elms[parent] > elms[Rchild]:
            temp = elms[Rchild]
            elms[Rchild] = elms[parent]
            elms[parent] = temp
            self.sort_heap(Rchild)

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
        TODO
        Put it in last element of list and do something like
        the opposite of sort heap (look at parent, swap with parent if needed
        until you don't need to swap with parent), switch index and recurse
        """

        pass
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
        TODO
        swap first and last element in list, delete new last element
        Then swap using sort_heap with index 0
        """
        pass
    def sorted_list(self):
        """
        returns a new list containing all the elements from min to max
        (O(n log n))
        TODO
        break down the tree from above
        make a copy of the heap
        then destroy the copy
        return the min (add it to the list)
        then delete the min 
        then sort the list

        """
        pass
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
            edge_spaces = 2**(height-i-1)-1 # calculates spaces
            in_spaces = 2**(height-i)-1
            mid_text = ""
            for j in range(2**i): # iterates
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
print(l2)

h = Heap(l2)
# print(h.list)
# while len(h.list) > 0:
#     h.display_heap()
#     h.list.pop()
# h.display_heap()
# print(h.root)


""" Hypothesis """
import pytest
from hypothesis import given
import hypothesis.strategies as st

@given(st.lists(st.integers()))
def test_heap_len(l):
    h = Heap(l)
    h.display_heap()
    print(len(l), h.length())
    assert len(l) == h.length()
