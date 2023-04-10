
class Graph():
    def __init__(self, file):
        self.vertex = {}
        self.edge = []
        
        self.read_file(file)
    
    def read_file(self, open_file):
        file = open(open_file,"r")
        
        edges = -1
        for line in file:
            if "*" in line:
                edges += 1
            
            elif not edges:
                vertex, label = line.split()
                vertex = int(vertex)
                self.vertex.update({vertex: {"label": label, "edge index": []}})

            elif edges:
                vertex, neighbor, weight = line.split()
                vertex = int(vertex)
                neighbor = int(neighbor)
                weight = float(weight)
                
                size = len(self.edge)

                neighbor_index = self.vertex.get(neighbor).get("edge index")
                neighbor_index.append(size)
                self.vertex.get(neighbor).update({vertex: weight, "edge index": neighbor_index})

                vertex_index = self.vertex.get(vertex).get("edge index")
                vertex_index.append(size)
                self.vertex.get(vertex).update({neighbor: weight, "edge index": vertex_index})
                self.edge.append((vertex, neighbor, weight))

    def get_vertex_quantity(self) -> int:
        return len(self.vertex.keys())
    
    def get_edge_quantity(self) -> int:
        return len(self.edge)
    
    def get_degree(self, vertex) -> int:
        return (len(self.vertex.get(vertex)) - 2)
    
    def get_label(self, vertex) -> str:
        return self.vertex.get(vertex).get("label")
    
    def get_neighbor(self, vertex):
        return      #ver aqui

    def get_edges(self, vertex_u, vertex_v) -> bool:
        return vertex_v in self.vertex.get(vertex_u)
    
    def get_weight(self, vertex_u, vertex_v) -> int:
        return self.vertex.get(vertex_u).get(vertex_v) #ver aqui
               
