"""
Homework 9
Data Structures and Algorithms
Katie Foster
"""
import numpy as np

def wrapper(s1, s2):
    answers = np.full([len(s1), len(s2)], -1)
    return wildcard(0, 0, s1, s2, answers)


def wildcard(i, j, s1, s2, answers):
    if answers[i, j] >= 0:
        return answers[i, j]
    if j==len(s2)-1 and s2[j]!= "*": # base case
        if s1[len(s1)-1] == s2[len(s2)-1] and i == len(s1)-1:
            answers[i, j] = True
            return True
        else:
            answers[i, j] = False
            return False
    elif j==len(s2)-1 and s2[j] == "*":
        answers[i, j] = True
        return True
    elif s1[i] == s2[j]:
        return wildcard(i+1, j+1, s1, s2, answers)
    elif s1[i] != s2[j]:
        if s1[i] == "*":
            for n in range(i+1, len(s1)):
                if wildcard(n, j+1, s1, s2, answers) == True:
                    answers[i, j] = True
                    return True
            answers[i, j] = False
            return False
        else:
            answers[i, j] = False
            return False




print(wrapper("lemondrop", "l*dr*p*"))


""" Test Function """
import pytest

def test_function():
    """ tests wildcard() function
    """
    assert wrapper("lemondrop", "l*dr*p*") == True, "Test one failed"
    assert wrapper("lemondrop", "l*mdr*p*") == False, "Test two failed"
    # assert , "Test three failed"


test_function()
