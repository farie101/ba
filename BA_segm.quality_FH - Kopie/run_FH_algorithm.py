from sort_edges import sort_edges
from component import Component
from union_find import UnionFind
from function import MInt
from FH_algo import FH
from ComponentManager import component_Manager
from grid_graph_builder import init_grid_graph
class FH_run():

    def __init__(self,img,k,type, mode, weight):
        self.img = img
        self.k =k
        self.type = type
        self.mode = mode
        self.weight = weight
        self.graph = None
        self.uf = None
    def init_graph(self):
         return init_grid_graph(self.type,self.img,self.mode, self.weight)
    def step_1(self):
        if self.graph is None:
            self.graph =  self.init_graph()
        self.graph =self.init_graph()
        return sort_edges(self.graph).get_sorted_edges()
    def step_2(self):
        if self.graph is None:
            self.graph =  self.init_graph()
        self.uf = UnionFind(len(self.graph.nodes))
        return component_Manager(self.graph,self.uf).init_segm()

    def step_3(self):
        edges = self.step_1()
        initial_S = self.step_2()
        return FH(self.graph,edges,initial_S,self.k,self.uf).step3()








