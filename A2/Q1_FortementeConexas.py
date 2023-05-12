# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1

from Q_Representacao import Graph

def ComponentesFortementeConexas(graph: Graph):
    arcsTrans = {}
    """for arc in graph.arcs:
        arcsTrans.append([arc[1], arc[0]])  #inverte direção do arco"""
    #print(arcsTrans)
    return graph.GetNeighborhoodTrans('a')

def DFS(graph: Graph):
    Cv = [] # Vertices visitados
    Tv = [] # Tempo
    Av = [] # Antecessor do vertice no caminho definido a partir de (s)
    
    s = graph.GetIndex(list(graph.adjList)[0])
    vertices = graph.GetVerticesQuantity()
    # Configurando todos os vértices
    for _ in range(vertices):
        Cv.append(False)
        Tv.append(float('inf'))
        Av.append(None)
    
    Cv[s-1] = True
    S = [] #pilha
    tempo = 0
    S.append(s)
    while len(S) != 0:
        tempo = tempo + 1
        u = S.pop()
        Tv[u-1] = tempo
        print("vizinhos: ", g.GetNeighborhood(g.GetLabel(u)))
        for vert in g.GetNeighborhood(g.GetLabel(u)):
            vert = g.GetIndex(vert)
            print("vert: ", vert)
            if Cv[vert-1] == False:
                Cv[vert-1] = True
                Av[vert-1] = u
                S.append(vert)
                print("Cv ", Cv)
                print("u ", u)
                print("S", S)
    print(Tv)
    return Av
 
if __name__ == '__main__':
    g = Graph()
    g.Read('GraphTest2.txt')
    print(ComponentesFortementeConexas(g))
    print(DFS(g))
