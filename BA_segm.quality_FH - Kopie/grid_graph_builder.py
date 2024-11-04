from PIL import Image
import networkx as nx
import Weight_Function


def addEdgestoGraph(G, img, mode, weight_function, i, x, y, width, height, graph_type):
    if (graph_type == 'Grid'):
        if x > 0:
            G.add_edge(i, i - 1, weight=weight_function.calculate_weight(img, mode, G, i, i - 1))
        if y > 0:
            G.add_edge(i, i - width, weight=weight_function.calculate_weight(img, mode, G, i, i - width))
        if x < width - 1 and y > 0:
            G.add_edge(i, i - (width - 1), weight=weight_function.calculate_weight(img, mode, G, i, i - (width - 1)))
        if x > 0 and y > 0:
            G.add_edge(i, i - (width + 1), weight=weight_function.calculate_weight(img, mode, G, i, i - (width + 1)))
    if(graph_type == 'NN'):
        pass


def init_grid_graph(graph_type, img, mode, weightfunction: Weight_Function):
    G = nx.Graph()
    width, height = img.size
    i = 0
    #i= y* width + x
    for y in range(height):
        for x in range(width):
            G.add_node(i, pos= (x,y))
            addEdgestoGraph(G,img, mode,weightfunction, i, x,y,width, height, graph_type)
            i+=1
    return G


