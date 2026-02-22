from collections import OrderedDict

def matrix_to_list(adj_matrix):
    """Converts Adjacency Matrix of graph to it's Adjacency List"""

    adj_list = {}
    for i, node in enumerate(adj_matrix):
        node_adj = []
        for j, connected_to in enumerate(node):
            if connected_to:
                node_adj.append(j)
                adj_list[i] = node_adj

    return adj_list

def list_to_path(trail):
    path = list(trail.keys())
    path.append(next(reversed(OrderedDict(trail).values())))
    return path
