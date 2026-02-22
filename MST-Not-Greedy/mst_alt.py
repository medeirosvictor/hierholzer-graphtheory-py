#!/usr/bin/python
from dfs import dfs_get_cycle

def mst_alt(graph, edges_weights):
    temp_tree = {k: [] for k in graph}
    mst = {}

    #Para cada aresta no conjunto de arestas
    for edge in edges_weights:

        #Adiciona arbitrariamente uma aresta
        print("Aresta inserida: ", edge, "Peso: ", edges_weights[edge])
        mst[edge] = edges_weights[edge]
        temp_tree[edge[0]].append(edge[1])
        temp_tree[edge[1]].append(edge[0])

        #Verifica se apos a adicao foi gerado um ciclo na solucao parcial
        cycle = dfs_get_cycle(mst)
        if cycle:
            print("ciclo encontrado", cycle)
            #Se existe um ciclo, remove a aresta de maior peso pertencente ao ciclo
            heaviest = cycle[0]
            for x in cycle:
                if edges_weights[heaviest] < edges_weights[x]:
                    heaviest = x
            temp_tree[heaviest[0]].remove(heaviest[1])
            temp_tree[heaviest[1]].remove(heaviest[0])
            mst.pop(heaviest)
            print("Aresta removida: ", heaviest, "Peso: ", edges_weights[heaviest])
        print("Solucao parcial MST: ", mst)
        print()

    #Resultado final
    print("Solucao final MST: ", mst)
    print("Peso total da MST obtida: ", sum(mst.values()))
    return mst
