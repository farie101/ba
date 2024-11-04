class sort_edges:
    def __init__(self, graph):
        self.graph = graph
    def sort_edges_by_weight(self):
        edges = list(self.graph.edges(data=True))
        edges_sorted = sorted(edges, key=lambda edge: edge[2]['weight'])

        return edges_sorted

    def get_sorted_edges(self):
        return self.sort_edges_by_weight()
