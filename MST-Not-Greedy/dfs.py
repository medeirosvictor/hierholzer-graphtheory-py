#!/usr/bin/python

cycles = []
#Inicializa busca por ciclos na solucao parcial apos insercao da nova aresta
def dfs_get_cycle(current_mst):
    global graph
    global cycles
    global p_edges
    p_edges = []
    graph = current_mst
    for edge in graph:
        for node in edge:
            find_cycle([node])
    return list(set(p_edges))

#Busca por ciclos em cada vertice
def find_cycle(path):
    start_node = path[0]
    next_node = None
    sub = []

    # visita cada aresta e cada vertice do conjunto de arestas
    # aresta = (x, y) -> node1 = x ; node2 = y
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
        if not visitado(next_node, path):
                sub = [next_node]
                sub.extend(path)
                find_cycle(sub)

        #Ciclo encontrado
        elif len(path) > 2 and next_node == path[-1]:
                p = ordena_ciclo_crescente(path)

                #adiciona todas as possiveis combinacoes de arestas
                # (0,1) e (1,0), por exemplo
                for x in range(0, len(p)-1):
                    if p[x] < p[x+1]:
                        p_edges.append((p[x], p[x+1]))
                    else:
                        p_edges.append((p[x + 1], p[x]))
                if p[0] < p[x+1]:
                    p_edges.append((p[0], p[x+1]))
                else:
                    p_edges.append((p[x + 1]), p[0])

def ordena_ciclo_crescente(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def visitado(node, path):
    return node in path
