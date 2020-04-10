"""
Homework 9
Data Structures and Algorithms
Katie Foster
"""
import numpy as np

def wrapper(s1, s2):
    answers = np.full([len(s1)+1, len(s2)+1], -1)
    return wildcard(0, 0, s1, s2, answers)


def wildcard(i, j, s1, s2, answers):
    if answers[i, j] != -1: # if answer has already been calculated, return it
        return answers[i, j]

    if j==len(s2): # base case
    # if we get to the end of s2, and it does not end in *
        if i == len(s1):
        # if we are also at the end of s1
            answers[i, j] = True
            return True
        else:
        # if we are not at the end of s1
            answers[i, j] = False
            return False

    # </base case> <general case>
    elif i<len(s1) and s1[i] == s2[j]:
    # if we have not reached the end, but the characters match
    # make recursive call with i and j incremented
        return wildcard(i+1, j+1, s1, s2, answers)

    elif i<len(s1) and s1[i] != s2[j]:
        # if we have not reached the end and the characters don't match

        if s2[j] == "*":
        # if s2[j] is a wildcard
        # increment i and check if i matches anything in s1
            for n in range(i, len(s1)+1):
                if wildcard(n, j+1, s1, s2, answers) == True:
                    # if there is a match, return true
                    answers[i, j] = True
                    return True
            # if no match, return false
            answers[i, j] = False
            return False
        else:
            # if s2[i] is not a wildcard, return false since they dont match
            # and no substituion can be made
            answers[i, j] = False
            return False
    else: # if you have reached the end of s1 but not s2
    # sort of another base case
        if s2[j] == "*":
            answers[i, j] = True
            return True
        else:
            answers[i, j] = False
            return False

print(wrapper("lemondrop", "l*dr*p*"))
print(wrapper("lemondrop", "l*mdr*p*"))

""" Test Function """
import pytest

def test_function():
    """ tests wildcard() function
    """
    assert wrapper("lemondrop", "l*dr*p*") == True, "Test one failed"
    assert wrapper("lemondrop", "l*mdr*p*") == False, "Test two failed"
    assert wrapper("blue", "*") == True, "Test three failed"
    assert wrapper("blue", "blue") == True, "Test four failed"
    assert wrapper("red", "blue") == False, "Test five failed"
    assert wrapper("red", "redorange") == False, "Test six failed"
    assert wrapper("", "") == True, "Test seven failed"
    assert wrapper("", "*") == True, "Test eight failed"
    assert wrapper("ab", "a*b") == True, "Test nine failed"
    assert wrapper("ab", "*ab") == True, "Test ten failed"


test_function()
