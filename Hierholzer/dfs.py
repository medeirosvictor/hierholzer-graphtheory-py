#!/usr/bin/python

from subtract_edges import subtract_edges
from converter import list_to_path

def dfs_cycle(graph, node, parent_node, start_node, sub_tour, cycle):
    """Modified DFS to get cycles"""
    if not cycle[0]:
        sub_tour.update({parent_node: node})
        for node_adj in graph[node]:
            if node_adj in sub_tour and node_adj == start_node and node_adj != parent_node:
                sub_tour.update({node: start_node})
                cycle[0] = sub_tour
            if node_adj not in sub_tour:
                dfs_cycle(graph, node_adj, node, start_node, sub_tour, cycle)
    else:
        return cycle[0]
