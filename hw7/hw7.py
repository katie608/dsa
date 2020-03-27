"""
Homework 7: Graphs
"""

""" Part 1 """
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



""" Part 2 """
