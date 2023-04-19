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

    r, cycle, C = buscarSubcicloEuleriano(graph, v, C)

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
#falta verificação

def buscarSubcicloEuleriano(graph: Graph, v: int, C: list) -> list:
    cycleS = [v] # Ciclo começando em v
    cycleT = []
    Cindex = 0

    u = v
    j = True

    while j:
        neighbors = graph.GetNeighborhood(graph.GetLabel(u))

        for i in range(len(neighbors)):
            neighbor = graph.GetIndex(neighbors[i])
            if (u, neighbor) or (neighbor, u) not in C:  
                C[Cindex] = (u, neighbor)   #representação das aresta é uma lista com dois vértices
                cycleS.append(neighbor)     #adiciona a pilha S

                u = neighbor
                Cindex += 1
                break

            elif i == len(neighbors):
                cycleT.append(cycleS.pop())     #remove pilha S e adiciona na pilha T
                u = cycleS(len(cycleS)-1)       #o vértice atual se torna a última posição acessada antes do ultim o vertice retirado, ou seja, vira o topo da pilha.
                #j = False

        if  not False in C:                     #se não tiver nenhum False no C acaba
            j = False


"""    t = v
    
    while True:
        
        
        
        if v == t:
            break
    
"""