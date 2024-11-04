from sort_edges import sort_edges
import networkx as nx
import unittest

class test_FH(unittest.TestCase):
    def setUp(self):
        self.g = nx.Graph()
        for i in range(100):
            self.g.add_node(i)
        self.sortedge = sort_edges(self.g)
    def test1_sort_edges(self):
        weight =20
        for i in range(10):
            self.g.add_edge(i,i+1,weight=weight)
            weight -= 1
        graph1 = self.sortedge.get_sorted_edges()
        self.assertEqual(graph1[9], (0 , 1, {'weight': 20}))
        self.assertEqual(graph1[0],(9,10,{'weight': 11}))
        self.g.add_edge(40,50,weight = 100)
        graph1 =self.sortedge.get_sorted_edges()
        self.assertEqual(graph1[10],(40,50,{'weight': 100}))
    def test2_sortedges(self):
        graph1 = self.sortedge.get_sorted_edges()
        self.assertEqual(graph1,[])
