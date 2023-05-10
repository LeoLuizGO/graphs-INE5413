# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1

from Q_Representacao import Graph

def ComponentesFortementeConexas(graph: Graph):
    arcsTrans = []
    for arc in graph.arcs:
        arcsTrans.append([arc[1], arc[0]])  #inverte direção do arco
    #print(arcsTrans)
    return graph.arcs

def DFS(graph: Graph):
    
    pass

if __name__ == '__main__':
    g = Graph()
    g.Read('GraphTest2.txt')
    print(ComponentesFortementeConexas(g))
