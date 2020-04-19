"""
Implementation of the Knapsack Problem
"""
import numpy as np

def wrapper(w, items):
    vals = np.full([w+1, len(items)+1], None)
    return knapsack(w, items, 0, vals)

def knapsack(w, items, i, vals):
    """
    w is remaining weight
    items is a list of (value, weight) tuples
    i is what item you are on
    """
    if vals[w, i] != None: # if answer has already been calculated, return it
        return vals[w, i]

    # base case: if algorithm is on the last item
    if i == len(items)-1:
        # take item if it is under weight limit
        if items[0][1] <= w:
            vals[w, i] = items[0][1]
            return items[0][1]
        # don't take item if it is over weight limit
        else:
            vals[w, i] = 0
            return 0

    # if weight of item > remaining weight
    if items[i][1] > w:
        vals[w, i] = knapsack(w, items, i+1)
        return knapsack(w, items, i+1, vals)

    # if weight of item < remaining weight
    else:
        dontInclude = knapsack(w, items, i+1, vals)
        include = knapsack(w, items, i, vals) + knapsack(w-items[i][1], items, i+1, vals)
        return max(dontInclude, include)



items = [(3, 1), (8, 2), (3, 4)]
print(wrapper(4, items))
