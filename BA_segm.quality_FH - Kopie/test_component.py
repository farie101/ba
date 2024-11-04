from component import Component
from union_find import UnionFind
import unittest
import networkx as nx
class test_component(unittest.TestCase):
    def setUp(self):
        self.componentsmap = {}
        self.uf = UnionFind(5)
        self.graph = nx.Graph
        self.c0 = Component(0, self.uf, self.componentsmap,self.graph)
        self.c1 = Component(1, self.uf, self.componentsmap, self.graph)
        self.c2 = Component(2, self.uf, self.componentsmap, self.graph)
        self.c3 = Component(3, self.uf, self.componentsmap, self.graph)
    def test_one_edge(self):
        self.c2.add_edge((2, 1))
        self.assertEqual(len(self.c2.nodes), 2, "Test 1 number nodes"
                         )
        self.assertEqual(self.c2.mst, [(2, 1)], "Test 1 mst")
        self.assertEqual(self.c2.max_edge_in_mst, (2, 1), "Test 1 mst")

    def test_edge_to_self(self):
        with self.assertRaises(ValueError):
            self.c0.add_edge((0, 0))


        self.assertEqual(len(self.c0.nodes), 1)

    def test_edge_with_node_not_in_C(self):
        with self.assertRaises(ValueError):
            self.c0.add_edge((3, 4))

        self.assertEqual(self.c0.mst, [])
    def test_edge_two_nodes_in_C(self):
        self.c0.add_edge((0, 1))
        self.c0.add_edge((1, 2))
        with self.assertRaises(ValueError):
            self.c0.add_edge((0, 2))
        self.assertEqual(self.c0.nodes, {0, 1, 2})
    def test_add_edge_other_c_deleted(self):
        self.c0.add_edge((0, 1))
        self.assertEqual(len(self.c1.nodes), 0)


    def test_merge_c_with_multiple_nodes(self):
        self.c0.add_edge((0,2))
        self.c1.add_edge((1,3))
        self.c0.add_edge((2,3))
        self.assertEqual(self.c0.nodes,{0,1,2,3})


if __name__ == '__main__':
    unittest.main()