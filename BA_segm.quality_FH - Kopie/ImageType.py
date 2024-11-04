from PIL import Image
from grid_graph_builder import init_grid_graph
import Absolute_Intensity
def identify_Image_Type(img: Image.Image, weight_Function):
    if(img.mode == 'L'):
        return init_grid_graph(img, 'L', weight_Function)
    if(img.mode == 'RGB'):
        graphR = init_grid_graph(img, 'R', weight_Function)
        graphG = init_grid_graph(img, 'G', weight_Function)
        graphB = init_grid_graph(img, 'B', weight_Function)
