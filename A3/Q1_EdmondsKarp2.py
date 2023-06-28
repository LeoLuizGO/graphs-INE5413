# Trabalho 3 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1 

from Representacao import Graph

def BFS_adapted(g: Graph, parent: list, quantityV: int) -> bool:
    V = [False]*quantityV
    
    Q = []
    Q.append(g.GetIndex("s"))
    V[g.GetIndex("s")-1] = True

    while Q:
        u = Q.pop()
        for neighbors in g.GetNeighborhood(g.GetLabel(u)):
            ind = g.GetIndex(neighbors)
            if V[ind-1] == False and g.GetWeight(u, ind) > 0:
                Q.append(g.GetIndex(neighbors))
                V[ind-1] = True
                parent[ind-1] = u

                if neighbors == "t":  #verificar se ta certo isso
                    return True
    return False

def edmondsKarp(g):
    quantityV = g.GetVerticesQuantity()
    parent = [-1]*quantityV

    max_flow = 0

    while BFS_adapted(g, parent, quantityV):
        path_flow = float("Inf")
        
        pass
    pass

if __name__ == '__main__':
    g = Graph()
    g.Read('fluxo_maximo_aula.net')
    #color, colors = welshPowell(g)
    #https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/