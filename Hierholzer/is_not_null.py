def is_not_null(graph):
    for node in graph:
        if len(graph[node]) != 0:
            return True
    print("Graph is null")
