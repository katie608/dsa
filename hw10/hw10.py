"""
Implementation of Travelling Salesman Heuristic Algorithm
Katie Foster
"""

import numpy as np
import time

def read_tsp(filename):
    ''' Reads a TSPLIB instance given by filename and returns the corresponding
    distance matrix C. Assumes that the edge weights are given in lower diagonal row
    form. '''

    f = open(filename,'r')

    n, C = 0, None
    i, j = -1, 0

    for line in f:
        words = line.split()
        if words[0] == 'DIMENSION:':
            n = int(words[1])
            C = np.zeros(shape=(n,n))
        elif words[0] == 'EDGE_WEIGHT_SECTION':
            i = 0 # Start indexing of edges
        elif i >= 0:
            for k in range(len(words)):
                if words[k] == 'EOF':
                    break
                elif words[k] == '0':
                    i += 1 # Continue to next row of the matrix
                    j = 0
                else:
                    C[i,j] = int(words[k])
                    C[j,i] = int(words[k])
                    j += 1
    return C, n

C, n = read_tsp('gr17.tsp')
# print(C)

def greedyHeuristic(C, num_nodes):
    """ Nearest Neighbor:
    starts at a city, keeps visiting next closest unvisited city repeatedly
    """
    path = []
    for i in range(num_nodes):
        dist = 9999999 # set initial distance to "infinity"
        nearest = None
        for j in range(num_nodes): # add the index of the min of C[i, :]
            if C[i, j] < dist and i != j and j not in path:
                print(dist, C[i, j], j)
                dist = C[i, j]
                nearest = j
        path.append(nearest)
    return path

print(greedyHeuristic(C, n))

# def localSearch(C, curr_path):
#     """ Starts with potential solution and looks for improvments until it can't
#     find any more improvments
#     2-opt: removes 2 edges then reconnects optimally
#     """
#     max_iterations = 20
#     for i in range(max_iterations):
#         # if no changes are made, break loop
#         for j in range(num_nodes):
#             for k in range(num_nodes):
#                 # swap two edges
#                 if new_dist > curr_dist:
#                     curr_path = new_path
#                     curr_dist = new_dist
#     return curr_path

def test():
    """ Tests runtime and optimality gaps of greedy heuristic and local search
    """
    pass
