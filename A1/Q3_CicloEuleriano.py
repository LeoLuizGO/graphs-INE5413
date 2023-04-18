#Questão 3

from Q1_Representacao import Graph

def CicloEuleriano(graph: Graph):
    Ce = []
    i = False
    j = 0

    for _ in range(graph.GetVerticesQuantity()):
        Ce.append(False)

    while i == False:
        vertex = j
        j += 1 

        if graph.GetNeighborhood(graph.GetLabel(vertex)) != []:
            i = True
        if j > graph.GetVerticesQuantity():
            return [False, None]

    v, cycle = buscarSubcicloEuleriano(graph, vertex)
    if v == False:
        return [False, None]
    else:
        pass        

def buscarSubcicloEuleriano(graph: Graph, ):
    pass
