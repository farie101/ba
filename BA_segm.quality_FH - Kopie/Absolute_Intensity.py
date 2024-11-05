from PIL import Image
import networkx as nx
from Weight_Function import Weight_Function
class AbsoluteIntensity(Weight_Function):
    @staticmethod
    def calculate_weight(img: Image.Image, mode, G: nx.Graph, i, j):
        pos_i = G.nodes[i]['pos']
        pos_j = G.nodes[j]['pos']
        pixel_i = img.getpixel(pos_i)
        pixel_j = img.getpixel(pos_j)
        weight = abs(pixel_i - pixel_j)
        return weight

