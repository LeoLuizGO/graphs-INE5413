# Questão 5
from Q1_Representacao import Graph

def floydWarshall(graph: Graph) -> list:
    quantVertices = graph.GetVerticesQuantity()
    D = [[float('inf')]*(quantVertices) for _ in range(quantVertices)]
    for i in range(quantVertices):
        for j in range(quantVertices):
            if i == j: 
                D[i][j] = 0
            else:
                D[i][j] = graph.GetWeight(graph.GetLabel(i+1), graph.GetLabel(j+1))
    for i in range(quantVertices):
        D = matrizPredecessora(D, i, quantVertices)
    return D, quantVertices

def matrizPredecessora(D: list, k: int, quantVertices: int) -> list:
    D1 = [[float('inf')]*(quantVertices) for _ in range(quantVertices)]
    for i in range(quantVertices):
        for j in range(quantVertices):
            if i == k or j == k or j==i:
                D1[i][j] = D[i][j]
            elif D[i][j] > D[i][k] + D[k][j]:
                D1[i][j] = D[i][k] + D[k][j]
            else: 
                D1[i][j] = D[i][j]
            
    return D1

if __name__ == "__main__":
    g = Graph()
    g.Read('GraphTest2.txt')
    D, quantVertices = floydWarshall(g)
    for i in range(quantVertices):
        print(f'{i+1}:{",".join(map(str, D[i]))}')
