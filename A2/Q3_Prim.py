# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 3

from Q_Representacao import Graph

def Prim(graph: Graph):
    vertices = graph.GetVerticesQuantity()
    Qv = []
    Av = []
    Kv = []

    for _ in range(vertices):
        Qv.append(False)
        Av.append(None)
        Kv.append(float('inf'))
    
    Kv[0] = 0
    while False in Qv:
        min = -1
        for i in range(vertices):
            if min == -1 and not(Qv[i]):
                min = Kv[i]
                u = i+1
            elif min < Kv[i] and not(Qv[i]):
                min = Kv[i]
                u = i+1
        uVert = graph.GetLabel(u)
        Qv[u-1] = True
        for neighbor in graph.GetNeighborhood(uVert):
            weight = graph.GetWeight(uVert, neighbor)
            if weight < Kv[graph.GetIndex(neighbor)-1]: 
                Av[graph.GetIndex(neighbor)-1] = u
                Kv[graph.GetIndex(neighbor)-1] = weight
    return Av

if __name__ == '__main__':
    g = Graph()
    g.Read('agm_tiny.txt')
    print(Prim(g))