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
        print("Initializing graph")
        graph = init_grid_graph(self.type,self.img,self.mode, self.weight)
        print(f"Graph created with {len(graph.nodes)} nodes and {len(graph.edges)} edges")
        return graph

    def step_1(self):
        print("Starting step_1")
        if self.graph is None:
            self.graph = self.init_graph()
        self.graph = self.init_graph()  # Note: You're initializing twice here
        edges = sort_edges(self.graph).get_sorted_edges()
        print(f"Step 1: Found {len(edges)} sorted edges")
        return edges
    def step_2(self):
        print("Starting step_2")
        if self.graph is None:
            self.graph = self.init_graph()
        self.uf = UnionFind(2*len(self.graph.nodes))
        initial_S = component_Manager(self.graph,self.uf).init_segm()
        print(f"Step 2: Created initial segmentation with {len(initial_S)} components")
        return initial_S

    def step_3(self):
        print("Starting step_3")
        edges = self.step_1()
        initial_S = self.step_2()
        print("About to call FH.step3()")
        result = FH(self.graph,edges,initial_S,self.k,self.uf).step3()
        print(f"Step 3 completed with {len(result)} components")
        return result









