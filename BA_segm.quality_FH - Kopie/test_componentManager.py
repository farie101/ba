import unittest
import networkx as nx
from ComponentManager import component_Manager
from union_find import UnionFind
from component import Component
class TestComponentManager(unittest.TestCase):

    def setUp(self):
        self.g = nx.Graph()
        for i in range(10):
            self.g.add_node(i)

        self.man = component_Manager(self.g, UnionFind(10))
    def test_t1(self):
        map = self.man.init_segm()
        self.assertEqual(len(map),10)

        for node in self.g.nodes:
            self.assertIn(node, map)
            self.assertIsInstance(map[node], Component)



