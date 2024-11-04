import unittest
import networkx as nx
from component import Component
from union_find import UnionFind
from FH_algo import FH
from sort_edges import sort_edges
from ComponentManager import component_Manager

class TestFHAlgo(unittest.TestCase):
    def setUp(self):
       self.graph = nx.Graph()
       for i in range(5):
            self.graph.add_node(i)
       self.graph.add_edge(1, 2, weight=0)
       self.graph.add_edge(0, 1, weight=10)
       self.graph.add_edge(2, 3, weight=2)
       self.graph.add_edge(3, 4, weight=1)
       self.uf = UnionFind(len(self.graph.nodes))
       self.edges = sort_edges(self.graph).get_sorted_edges()
       self.S = component_Manager(self.graph, self.uf).init_segm()
       self.k = 80
       self.fh_algo = FH(self.graph,self.edges, self.S, self.k, self.uf)


    def test_initialization_of_S(self):
        # Überprüfe, dass jeder Knoten im Graphen in S enthalten ist
        for node in self.graph.nodes:
            self.assertIn(node, self.S, f"Knoten {node} sollte in der Komponenten-Map S sein")
            self.assertIsInstance(self.S[node], Component,
                                  f"Eintrag für Knoten {node} sollte eine Component-Instanz sein")

    def test_merge_components_in_S(self):
        # Stelle sicher, dass vor dem Merge jede Komponente separat ist
        initial_component_count = len(set(self.uf.find(node) for node in self.graph.nodes))
        self.assertEqual(initial_component_count, 5, "Es sollten vor dem Merge 5 separate Komponenten vorhanden sein.")

        merged_S = self.fh_algo.step3()


        print("Inhalt von merged_S nach step3:", merged_S.keys())
        # Überprüfe, dass am Ende nur eine Komponente in S existiert
        final_component_count = len(set(self.uf.find(node) for node in self.graph.nodes))
        self.assertEqual(final_component_count, 1, "Es sollte nur eine Komponente nach dem Merge existieren.")

        # Optional: Überprüfe die Struktur in S, ob alle Knoten zur gleichen Komponente gehören
        for node in self.graph.nodes:
            self.assertEqual(merged_S[self.uf.find(0)], merged_S[self.uf.find(node)],
                             f"Knoten {node} sollte zur gleichen Komponente wie Knoten 0 gehören.")

    def test_no_circles(self):
        self.graph.add_edge(3,1,weight=2)
        self.fh_algo = FH(self.graph, self.edges, self.S, self.k, self.uf)
        merged_S = self.fh_algo.step3()
        self.assertCountEqual(merged_S[1].mst, [(1, 2), (3, 4), (2, 3), (0, 1)])

    def test_newgraph_präsi(self):
        graph = nx.Graph()
        graph.add_edge(1,0, weight = 40)
        graph.add_edge(2,1, weight = 55)
        graph.add_edge(3,0, weight = 5)
        graph.add_edge(4,1,weight= 10)
        graph.add_edge(5,2,weight= 15)
        graph.add_edge(4,3,weight= 45)
        graph.add_edge(5,4,weight= 80)
        graph.add_edge(8,5,weight= 205)
        graph.add_edge(7,4,weight= 105)
        graph.add_edge(6,3,weight= 75)
        graph.add_edge(7,6,weight= 75)
        graph.add_edge(8,7,weight= 20)
        uf = UnionFind(len(graph.nodes))
        edges = sort_edges(graph).get_sorted_edges()
        S = component_Manager(graph, uf).init_segm()
        k = 80
        merged_S= FH(graph,edges,S,k,uf).step3()
        self.assertEqual(len(merged_S),3)
        actual_mst = [(min(u, v), max(u, v)) for u, v in merged_S[1].mst]
        self.assertCountEqual(actual_mst,[(0, 3), (0, 1), (1, 2), (1, 4), (2, 5)])
        actual_mst1 = [(min(u, v), max(u, v)) for u, v in merged_S[6].mst]
        self.assertEqual(actual_mst1,[])
        actual_mst2 = [(min(u, v), max(u, v)) for u, v in merged_S[8].mst]
        self.assertEqual(actual_mst2,[(7,8)])
        self.assertEqual(merged_S[1].nodes, {0, 1, 2, 3, 4, 5})
        self.assertEqual(merged_S[6].nodes, {6})
        self.assertEqual(merged_S[8].nodes, {7,8})


    # Test ausführen
if __name__ == '__main__':
    unittest.main()