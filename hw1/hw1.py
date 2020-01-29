

def longest_increasing_sequence(list):
    """
    takes in a list of integers and returns the longest strictly
    increasing subsequence
    """

    longest_seq = []
    seq = []
    for i in range (len(list)): # itereates through entire list
        if list[i] > list[i-1]: # if value is greater than value behind it
            seq.append(list[i]) # add that value to the sequence
        elif list[i] <= list[i-1]: # if value is less than value behind it
            if len(seq) >= len(longest_seq):
                longest_seq = seq #replace the longest sequence with the working sequence if neccesary
            seq = [list[i]]
    if len(seq) >= len(longest_seq):
        longest_seq = seq #replace the longest sequence with the working sequence if neccesary
    return longest_seq


# test using pytest test function
import pytest
def test_function():
	assert longest_increasing_sequence([3, 1, 2, 3, 5, 8, 2]) == [1, 2, 3, 5, 8],"test failed"
	assert longest_increasing_sequence([1, 2, 0, 4, 8, 9, 3]) == [0, 4, 8, 9],"test failed"
	assert longest_increasing_sequence([]) == [],"test failed"
	assert longest_increasing_sequence([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],"test failed"
	assert longest_increasing_sequence([4, 3, 0, 0]) == [0],"test failed"
	assert longest_increasing_sequence([1, 2, 3, 4, 5, 6, 3, 4, 5]) == [1, 2, 3, 4, 5, 6],"test failed"
