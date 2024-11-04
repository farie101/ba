import networkx as nx
import grid_graph_builder
from PIL import Image
from Weight_Function import Weight_Function


class AbsoluteIntensity(Weight_Function):
    @staticmethod
    def calculate_weight(img: Image.Image, mode, G: nx.Graph, i, j):
        pos_i = G.nodes[i]['pos']
        pos_j = G.nodes[j]['pos']

        pixel_i = img.getpixel(pos_i)
        pixel_j = img.getpixel(pos_j)

        if mode == 'L':
            if isinstance(pixel_i, tuple):
                pixel_i = sum(pixel_i) / len(pixel_i)
            if isinstance(pixel_j, tuple):
                pixel_j = sum(pixel_j) / len(pixel_j)
            return abs(pixel_i - pixel_j)

        channel_map = {'R': 0, 'G': 1, 'B': 2}
        if mode in channel_map:
            intensity_i = pixel_i[channel_map[mode]]
            intensity_j = pixel_j[channel_map[mode]]
            return abs(intensity_i - intensity_j)


