from function import MInt
from union_find import UnionFind
from component import Component
class FH():
    def __init__(self, graph, edges_list, S, k, union):
        self.edges = edges_list
        self.graph =graph
        self.S = S
        self.uf = union
        self.k = k
    def step3(self):
        for u, v, data in self.edges:
            weight = data['weight']
            component_u = self.S[self.uf.find(u)]
            component_v = self.S[self.uf.find(v)]
            if component_u != component_v:
                if weight <= MInt(component_u,component_v,self.k):
                    component_u.add_edge((u,v))
        return self.S

