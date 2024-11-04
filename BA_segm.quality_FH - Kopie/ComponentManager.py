from component import Component
from union_find import UnionFind
class component_Manager():
    def __init__(self, graph, unionfind):
        self.g = graph
        self.uf = unionfind

    def init_segm(self):
        n = len(self.g.nodes)

        S = {}
        for node in self.g.nodes:
            S[node] = Component(node, self.uf, S, self.g)
        return S
