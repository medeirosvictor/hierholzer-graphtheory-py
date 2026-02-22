def matrix_to_list(adj_matrix):
    """Converts Adjacency Matrix of graph to it's Adjacency List"""

    adj_list = {}
    edges_weighted = {}
    for i, node in enumerate(adj_matrix):
        node_adj = []
        for j, connected_to in enumerate(node):
            if connected_to != 'inf' and i != j:
                node_adj.append(j)
                adj_list[i] = node_adj
                if i < j:
                    edges_weighted[i, j] = int(connected_to)

    return adj_list, edges_weighted
