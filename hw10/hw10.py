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

def get_distance(C, path):
    """ Returns the sum of all the edge lengths in a certain path
    """
    dist = 0
    for i in range(len(path)):
        dist += C[i, path[i]]
    return dist


def greedyHeuristic(C, num_nodes):
    """ Nearest Neighbor:
    starts at the first city, repeatedly adds the closest unvisited city, until
    the path has visited all cities
    This is the greediest of algorithms, because it adds the closest city, which
    will optimize the path in the short term, but does not make any long term
    calculations at all.
    """
    path = []
    total_dist = 0
    for i in range(num_nodes):
        dist = 9999999 # set initial distance to "infinity"
        nearest = None
        for j in range(num_nodes): # add the index of the min of C[i, :]
            if C[i, j] < dist and i != j and j not in path:
                dist = C[i, j]
                nearest = j
        path.append(nearest)
        total_dist += dist
    return path, total_dist

path, total_dist = greedyHeuristic(C, n)
print(path, total_dist)
# print(get_distance(path, C))

def localSearch(C, curr_path):
    """ Starts with potential solution and looks for improvments until it can't
    find any more improvments
    curr_path is a python list of nodes, representing a path
    2-opt: removes 2 edges then reconnects optimally
    """
    num_nodes = len(curr_path)
    max_iterations = 20
    curr_dist = get_distance(C, curr_path)
    for i in range(max_iterations):
        # if no changes are made, break loop
        for j in range(num_nodes):
            for k in range(num_nodes):
                # swap two edges
                new_path = curr_path
                new_path[k-1] = curr_path[k]
                new_path[k] = curr_path[k-1]
                new_dist = get_distance(C, new_path)
                # print(new_dist)
                if new_dist < curr_dist:
                    curr_path = new_path
                    curr_dist = new_dist
    return curr_path, curr_dist

print(localSearch(C, path))

def test():
    """ Tests runtime and optimality gaps of greedy heuristic and local search
    """
    pass
