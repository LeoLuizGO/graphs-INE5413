# Questão 4

from Q1_Representacao import Graph

def BellmanFord(grafo: Graph, s: int) -> tuple :
    D = [] # Lista de pesos dos caminhos ( s , v )
    A = [] # Lista de antecessores
    
    # Inicialização
    for i in range(grafo.GetVerticesQuantity()):
        D.append(float('inf'))
        A.append(None)
        
    D[s] = 0
    
    for i in range(1, grafo.GetVerticesQuantity()-1):
        for j in range(grafo.GetEdgesQuantity()):
            # Relaxamento
            