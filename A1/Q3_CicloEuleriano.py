# Questão 3

from Q1_Representacao import Graph



def CicloEuleriano(graph: Graph):
    C = [] # Vetor de arestas visitadas
    i = False
    j = 0

    for _ in range(graph.GetEdgesQuantity()):
        C.append(False)

    while i == False:
        v = j  # Vertice arbitrario
        j += 1

        # Escolha arbitraria do vertice que possui alguma aresta
        if graph.GetNeighborhood(graph.GetLabel(v)) != []:
            i = True
        if j > graph.GetVerticesQuantity():
            return [False, None]

    r, cycle = buscarSubcicloEuleriano(graph, v, C)

    if r == False:
        return [False, None]

    else:
        condition = False

        for edge in C:
            if edge == False:
                condition == True
                break

        if condition:
            return (False, None)

        else:
            return (True, cycle)


def buscarSubcicloEuleriano(graph: Graph, v: int, C: list) -> list:
    cycle = [v] # Ciclo começando em v
    t = v
    
    while True:
        
        
        
        if v == t:
            break
    
