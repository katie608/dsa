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

C, n = read_tsp("gr17.tsp")

def get_distance(C, path):
    """ Returns the sum of all the edge lengths in a certain path
    """
    dist = 0
    for i in range(len(path)-1):
        dist += C[path[i], path[i+1]]
    dist += C[path[len(path)-1], path[0]] 
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
        dist = float('inf') # set initial distance to infinity
        nearest = None
        for j in range(num_nodes): # add the index of the min of C[i, :]
            if C[i, j] < dist and i != j and j not in path:
                dist = C[i, j]
                nearest = j
        path.append(nearest)
        total_dist += dist
    return path, get_distance(C, path)

path, dist = greedyHeuristic(C, n)
print(path, dist)
# print(len(set(path)) == len(path))
# print(len(path) == n)

def localSearch(C, curr_path):
    """ Starts with potential solution and looks for improvments until it can't
    find any more improvments
    curr_path is a python list of nodes, representing a path
    2-opt: removes 2 edges then reconnects optimally
    """

    num_nodes = len(curr_path)
    max_iterations = 100
    curr_dist = get_distance(C, curr_path)
    for i in range(max_iterations):
        # if no changes are made, break loop
        for j in range(num_nodes):
            for k in range(j, num_nodes): # might need j+1
                # swap two edges
                new_path = curr_path[:]
                new_path[k-1] = curr_path[k]
                new_path[k] = curr_path[k-1]
                new_dist = get_distance(C, new_path)
                # check to make sure it is not added twice?
                if new_dist < curr_dist and len(set(new_path)) ==  len(new_path):
                    curr_path = new_path
                    curr_dist = new_dist
    return curr_path, int(curr_dist)




def test():
    """ Tests runtime and optimality gaps of greedy heuristic and local search

    """
    optimal_distances = {
        "gr17": 2085,
        "gr21": 2707,
        "gr24": 1272,
        "gr48": 5046
    }

    filenames = ['gr17.tsp', 'gr21.tsp', 'gr24.tsp', 'gr48.tsp']
    for file in filenames:
        print(file, ":")
        C, n = read_tsp(file)
        optimal_dist = optimal_distances[file[0:4]]
        path, heuristic_dist = greedyHeuristic(C, n)
        print("Distance from Greedy Heuristic:", heuristic_dist)
        print("Greedy Heuristic optimality ratio:", (heuristic_dist-optimal_dist)/optimal_dist)
        local_dist = localSearch(C, path)[1]
        print("Distance from Local Search:", local_dist)
        print("Local Search optimality ratio:", (local_dist-optimal_dist)/optimal_dist)
        print("Optimal Distance:", optimal_dist)
        print("")

test()

"""
Results from test:

gr17.tsp :
Distance from Greedy Heuristic: 4865.0
Greedy Heuristic optimality ratio: 1.3333333333333333
Distance from Local Search: 4220
Local Search optimality ratio: 1.023980815347722
Optimal Distance: 2085

gr21.tsp :
Distance from Greedy Heuristic: 7320.0
Greedy Heuristic optimality ratio: 1.7041004802364241
Distance from Local Search: 5422
Local Search optimality ratio: 1.0029553010712966
Optimal Distance: 2707

gr24.tsp :
Distance from Greedy Heuristic: 3446.0
Greedy Heuristic optimality ratio: 1.7091194968553458
Distance from Local Search: 2784
Local Search optimality ratio: 1.1886792452830188
Optimal Distance: 1272

gr48.tsp :
Distance from Greedy Heuristic: 19273.0
Greedy Heuristic optimality ratio: 2.8194609591755846
Distance from Local Search: 15128
Local Search optimality ratio: 1.9980182322631788
Optimal Distance: 5046

It seems like my greedy heurisitc algorithm does a decent job with smaller
datasets, but does a really bad job with big sets. Also the local search
helps optimize the algorithm in every instance, which is good.

"""
