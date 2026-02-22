def subtract_edges(graph_1, graph_2):
    for node_2 in graph_2:
        for node_1 in graph_1:
            if node_1 == node_2:
                edges_in_node = graph_1.get(node_1)
                for edge in edges_in_node:
                    if edge == graph_2.get(node_2):
                        graph_1[node_1].remove(edge)
            elif graph_2.get(node_2) == node_1:
                graph_1.get(node_1).remove(node_2)
    return graph_1
