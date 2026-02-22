#!/usr/bin/python

from read_input import read_file
from converter import matrix_to_list
from mst_alt import mst_alt


def main():
    graph_size, adj_matrix = read_file()
    graph, edges_weights = matrix_to_list(adj_matrix)
    print("Graph: ", graph)
    print("Edges: ", edges_weights)
    mst_alt(graph, edges_weights)

if __name__ == '__main__':
    main()
