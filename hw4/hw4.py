"""
3. Implementation of function from part 1.
"""

def zero_sum(list):
    """
    returns sum of list if list contains elements, returns 0 otherwise
    """
    if not list:
        return 0
    else:
        return sum(list)

def best_interval(list):
    """
    returns consecutive interval with greatest overall value
    list: a python list of integers
    """
    if len(list) == 1:
        # base case: list is only one element
        if list[0] > 0:
            # if list element is positive, return the list
            # print(list, list)
            return list, list
        if list[0] <= 0:
            # if the list element is negative, return empty lists
            # print([], [])
            return [], []
    # l1 is current best list
    # l2 is best list that includes the last element in the current list
    l1, l2 = best_interval(list[:-1])
    if zero_sum(l1) < zero_sum(l2) + list[len(list)-1]:
        # if sum of l1 is less than sum of l2+last element in currrent list
        l1 = l2 + [list[len(list)-1]] # set l1 = l2+last element in current list
    if (zero_sum(l2)+list[len(list)-1]) < 0:
        # if the sum of l2+last element is negative, set l2 to empty list
        l2 = []
    else:
        # if the sum is positive, add last element to l2
        l2.append(list[len(list)-1])
    # print(l1, l2)
    return l1, l2


# print("Answer: ", best_interval(one)[0])


""" Test Function """
import pytest

def test_function():
    """ tests best_interval function
    """
    one = [2, -6, 7, 8, -10, 0, 5, 3]
    two = [2, -6, 4, 8, -10, 4]
    three= [0, 0, -2]
    assert best_interval(one)[0] == [7, 8], "Test one failed"
    assert best_interval(two)[0] == [4, 8], "Test two failed"
    assert best_interval(three)[0] == [], "Test three failed"


test_function()


"""
4.
"""

import random

def four():
    avglen = 0
    avgval = 0
    for i in range (100):
        l = []
        for i in range (100):
            l.append(random.randint(-10, 10))
        b = best_interval(l)[0]
        print("Length: ", len(b))
        avglen += len(b)/100
        avgval += sum(b)/100
    print("Average Length: ", avglen)
    print("Average Value: ", avgval)


"""
5.
"""

import numpy as np

def five():
    avglen = 0
    avgval = 0
    for i in range (100):
        l = []
        # np.random.normal(mu, sigma, number)
        # mu is mean, sigma is standard deviation
        npl1 = np.random.normal(6, 1, 70)
        npl2 = np.random.normal(-7, 0.5, 30)
        npl = np.concatenate((npl1, npl2), axis=0)
        np.random.shuffle(npl)
        print(npl)
        l = npl.tolist()
        b = best_interval(l)[0]
        print("Length: ", len(b))
        avglen += len(b)/100
        avgval += sum(b)/100
    print("Average Length: ", avglen)
    print("Average Value: ", avgval)



five()

    
