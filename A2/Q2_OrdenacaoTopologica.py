# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 2

from Q_Representacao import Graph

def OrdenacaoTopologica (graph: Graph) -> list:
    C = [] # vértices visitados
    T = [] # tempo inicial do vertice
    F = [] # tempo final do vertice
    
    for _ in range(graph.GetVerticesQuantity()):
        C.append(False)
        T.append(float('inf'))
        F.append(float('inf'))
        
    time = 0 # tempo inicial
    O = [] # Ordenação topológica
    
    for u in range(graph.GetVerticesQuantity()):
        if C[u] == False:
            dfsVisitOT(graph, u, C, T ,F, time, O)
            
    return O

def dfsVisitOT (graph: Graph, v: int, C: list, T: list, F: list, time: int, O: list) -> None:
    C[v] = True
    time += 1
    T[v] = time
    
    for neighbor in graph.GetNeighborhood(graph.GetLabel(v + 1)):
        if C[graph.GetIndex(neighbor) - 1] == False:
            dfsVisitOT(graph, (graph.GetIndex(neighbor)-1), C, T ,F, time, O)
            
    time += 1
    F[v] = time
    O.insert(0, graph.GetLabel(v + 1))
    
if __name__ == "__main__":
    g = Graph()
    g.Read("manha.net")
    O = OrdenacaoTopologica(g)
    
    for vertex in range(len(O)):
        print(f'{O[vertex]}', end='')
        if vertex < len(O) - 1:
            print(' -> ', end='')