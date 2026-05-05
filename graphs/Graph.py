

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_edge(self, edge_from, edge_to, wheight:int = None):
        self.nodes.append(edge_from, edge_to)
        self.edges.append((edge_from, edge_to, wheight))

    def add_edges(edges: list):
        pass

    
G = Graph()

G.add_edge("A", "B", 10)