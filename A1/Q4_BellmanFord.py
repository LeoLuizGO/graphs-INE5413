# Questão 4


# VERIFICAR PQ A SAIDA TA ERRADA, OS DADOS NAO TAO SENDO GRAVADOS NA LISTA D E NA LISTA A

from Q1_Representacao import Graph

def BellmanFord(graph: Graph, s: int) -> tuple():
    D = [] # Lista de pesos dos caminhos ( s , v )
    A = [] # Lista de antecessores
    
    # Inicialização
    for i in range(graph.GetVerticesQuantity()):
        D.append(float('inf'))
        A.append(None)
    
    D[s - 1] = float(0)
    
    # Relaxamento
    for _ in range(graph.GetVerticesQuantity() - 1):
        for vertex in range(1, graph.GetVerticesQuantity() + 1):
            for neighbor in graph.GetNeighborhood(graph.GetLabel(vertex)):
                if D[vertex-1] > D[vertex-1] + graph.GetWeight(graph.GetLabel(vertex), neighbor):
                    D[vertex-1] = D[graph.GetIndex(neighbor)] + graph.GetWeight(graph.GetLabel(vertex), neighbor)
                    A[vertex-1] = graph.GetIndex(neighbor)
                    
    # Verificação de ciclos negativos 
    for vertex in range(1, graph.GetVerticesQuantity() + 1):
        for neighbor in graph.GetNeighborhood(graph.GetLabel(vertex)):
            if D[vertex - 1] + graph.GetWeight(graph.GetLabel(vertex), neighbor) < D[vertex - 1]:
                return (False, None, None)
            
    return (True, D, A)

if __name__ == "__main__":
    g = Graph()
    g.Read('GraphTest1.txt')
    cycle, D, A = BellmanFord(g, 1)
    if cycle:
        print(f'D = {D}')
        print(f'A = {A}\n')
    
    else:
        print('Tem ciclo negativo')
    
    