#!/usr/bin/python

from read_input import read_file
from converter import matrix_to_list
from hierholzer import hierholzer
from is_connected import is_connected
from is_eulerian_graph import is_eulerian_graph
from is_semi_eulerian_graph import is_semi_eulerian_graph

def main():
    """Read file input
       Convert adjacency matrix to adjacency list and use it as main graph data structure
       Call Hierholzer Algorithm"""

    graph_size, adj_matrix = read_file()
    graph = matrix_to_list(adj_matrix)
    is_connected(graph)
    is_eulerian_graph(graph)
    odd_vertex = is_semi_eulerian_graph(graph)
    start_vertex = 0 if odd_vertex is None else odd_vertex[0]
    print("Euler Tour: ", hierholzer(graph, start_vertex))


if __name__ == '__main__':
    main()
