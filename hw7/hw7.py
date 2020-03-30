"""
Homework 7: Graphs
"""

""" Part 2 """
import networkx as nx

def find_components(G):
    """ counts number of times Depth First Search is called on a graph
    in order to determine number of components in a graph
    """
    nodes = G.nodes()
    num_nodes = len(nodes)
    num_components = 0 # initialize counter of number of components
    unvisited_list = list(nodes) # Mark all nodes as unvisited
    while len(unvisited_list) > 0: # while there are unvisited nodes
        DFS(G, unvisited_list[0], unvisited_list)
        num_components +=1
    return num_components

def DFS(G, u, unvisited_list):
    """ implementation of depth first search on a graph
    """
    unvisited_list.remove(u) # mark u as visited
    for neighbor in G.neighbors(u): # go through u's neighbors
        if neighbor in unvisited_list: # if neighbor is unvisited
            DFS(G, neighbor, unvisited_list) # call DFS on neighbor
    return unvisited_list

""" Test Function for part 1"""
import pytest

def test_function():
    """
    """
    G = nx.Graph()
    G.add_node(1) # adds node with label 1
    G.add_node(2) # adds node with label 2
    G.add_edge(1,2) # adds an undirected edge between nodes 1 and 2
    assert find_components(G) == 1, "Test one failed"
    G.add_node(3)
    assert find_components(G) == 2, "Test two failed"
    G.add_node(4)
    assert find_components(G) == 3, "Test three failed"

test_function()



""" Part 3 """
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_binomial_graph(num_nodes, p):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if np.random.randint(0, 1/p) == 1: # make a choice
            # basically roll a p sided die, and add edge if number is 1
                G.add_edge(i, j)
    return G


def generate_random_graphs():
    x = []
    y = []
    for i in range(45):
        for j in range(1, 101):
            k = 0
            num_components = 1
            while num_components == 1:
                # exit loop if any graph has more than 1 component
                G = generate_random_binomial_graph(i+5, j/100)
                num_components = find_components(G)
                k+=1
                # count number of times loop has run, if loop has run all 10 times
                # that means that all 10 graphs have 1 component,
                # so add that entry to graph lists
                if k == 10:
                    x.append(i) # i is num_nodes (5-50)
                    y.append(j/100) # j is probability (1-100)
                    break
    return x, y


def graph_smallest_prob():
    x, y = generate_random_graphs()
    plot = plt.plot(x, y)


    plt.show()

graph_smallest_prob()
# g = generate_random_binomial_graph(4, 0.4)
# print(g.nodes(), g.edges())
