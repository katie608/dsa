

def longest_increasing_sequence(list):
    """
    takes in a list of integers and returns the longest strictly
    increasing subsequence

    >>> longest_increasing_sequence([3, 1, 2, 3, 5, 8, 2])
    [1, 2, 3, 5, 8]

    >>> longest_increasing_sequence([1, 2, 0, 4, 8, 9, 3])
    [0, 4, 8, 9]

    >>> longest_increasing_sequence([])
    []

    >>> longest_increasing_sequence([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    >>> longest_increasing_sequence([4, 3, 0, 0])
    [0]

    >>> longest_increasing_sequence([1, 2, 3, 4, 5, 6, 3, 4, 5])
    [1, 2, 3, 4, 5, 6]

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
