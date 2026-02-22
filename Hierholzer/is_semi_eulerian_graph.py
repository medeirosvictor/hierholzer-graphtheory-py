def is_semi_eulerian_graph(graph):
    odd_node = []
    for node in graph:
        if len(graph[node]) % 2 != 0:
            odd_node.append(graph[node])
    if len(odd_node) != 2:
        print("Graph is not Semi-Eulerian")
    else:
        return odd_node
