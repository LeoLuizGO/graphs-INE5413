
class Graph():
    def __init__(self, file):
        self.vertex = {}
        self.edge = []

        self.read_file(file)

    def read_file(self, open_file):
        file = open(open_file, "r")

        edges = -1
        for line in file:
            if "*" in line:
                edges += 1

            elif not edges:
                vertex, label = line.split()
                vertex = vertex
                self.vertex.update({vertex: {"label": label, "edgeIndex": []}})

            elif edges:
                vertex, neighbor, weight = line.split()
                vertex = vertex
                neighbor = neighbor
                weight = float(weight)

                size = len(self.edge)

                neighbor_index = self.vertex[neighbor]["edgeIndex"]
                neighbor_index.append(size)
                self.vertex.get(neighbor).update(
                    {vertex: weight, "edgeIndex": neighbor_index})

                vertex_index = self.vertex[vertex]['edgeIndex']
                vertex_index.append(size)
                self.vertex.get(vertex).update(
                    {neighbor: weight, "edgeIndex": vertex_index})
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
        return  # ver aqui

    def get_edges(self, vertex_u, vertex_v) -> bool:
        return vertex_v in self.vertex.get(vertex_u)

    def get_weight(self, vertex_u, vertex_v) -> int:
        return self.vertex.get(vertex_u).get(vertex_v)  # ver aqui
