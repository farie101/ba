import unittest
from grid_graph_builder import init_grid_graph
from PIL import Image
import networkx as nx
from placeholder import placeholder
class TestGridGraphBuilder(unittest.TestCase):
    def setUp(self):

        self.img = Image.new('L', (3, 3), "white")  # 3x3 weißes Bild
        self.weight_function = placeholder()


    def test_A_3x3_image_creates_9_nodes(self):
        graph = init_grid_graph('Grid',self.img,'L', self.weight_function)
        self.assertEqual(len(graph.nodes), 9)
    def test_A_3x3_image_crates_20_edges(self):
        graph = init_grid_graph('Grid',self.img,'L', self.weight_function)
        self.assertEqual(len(graph.edges),20)
    def test_A_100x100_image_is_correct(self):
        self.img1=Image.new('L', (100, 100), "white")
        graph = init_grid_graph('Grid', self.img1,'L', self.weight_function)
        self.assertEqual(len(graph.nodes), 10000)
        self.assertEqual(len(graph.edges), 39402)
        self.assertEqual(graph.degree(0),3)
        self.assertEqual(graph.degree(3),5)
        self.assertEqual(graph.degree(205),8)

    def test_empty_image(self):
        self.img2=Image.new('L',(0,0),"black")
        graph = init_grid_graph('Grid',self.img2,'L', self.weight_function)
        self.assertEqual(len(graph.nodes), 0)

    def test_1pixel_image(self):
        self.img2 = Image.new('L', (1, 1), "black")
        graph = init_grid_graph('Grid', self.img2,'L', self.weight_function)
        self.assertEqual(len(graph.nodes), 1)
        self.assertEqual(len(graph.edges), 0)
