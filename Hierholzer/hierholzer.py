#!/usr/bin/python

from subtract_edges import subtract_edges
from is_not_null import is_not_null
from dfs import dfs_cycle
from converter import list_to_path

def hierholzer(graph, node):
    euler_tour = []
    parent_node = node
    start_node = node
    callback = [False]
    dfs_cycle(graph, node, parent_node, start_node, {}, callback)
    sub_tour = callback[0]
    cycle = list_to_path(sub_tour)
    if not cycle:
        print("Graph is acyclic")
        return euler_tour
    print("Cycle found: ", cycle)
    euler_tour = cycle + euler_tour
    print("Eulerian Tour at the moment: ", euler_tour)
    graph = subtract_edges(graph, sub_tour)
    while is_not_null(graph):
        check = False
        for node in graph:
            if len(graph[node]) > 0:
                check = True
                current_node = node
                break
        if not check:
            print("Graph is not eulerian")
            return False
        callback = [False]
        dfs_cycle(graph, current_node, current_node, current_node, {}, callback)
        sub_tour = callback[0]
        cycle = list_to_path(sub_tour)
        print("Cycle found: ", cycle)
        if not cycle:
            return euler_tour
        pos = euler_tour.index(current_node)
        euler_tour[pos:pos+1] = cycle
        print("Eulerian Tour at the moment: ", euler_tour)
        graph = subtract_edges(graph, sub_tour)

    return euler_tour
