from PIL import Image
import networkx as nx
import Weight_Function




def init_grid_graph(graph_type, img, mode, weightfunction: Weight_Function):
    print(f"Initializing grid graph: type={graph_type}, mode={mode}")
    G = nx.Graph()
    width, height = img.size
    print(f"Image size: {width}x{height}")
    i = 0
    for y in range(height):
        for x in range(width):
            G.add_node(i, pos=(x,y))
            if x > 0:
                weight = weightfunction.calculate_weight(img, mode, G, i, i - 1)
                G.add_edge(i, i - 1, weight=weight)
            if y > 0:
                weight = weightfunction.calculate_weight(img, mode, G, i, i - width)
                G.add_edge(i, i - width, weight=weight)
            if x < width - 1 and y > 0:
                weight = weightfunction.calculate_weight(img, mode, G, i, i - (width - 1))
                G.add_edge(i, i - (width - 1), weight=weight)
            if x > 0 and y > 0:
                weight = weightfunction.calculate_weight(img, mode, G, i, i - (width + 1))
                G.add_edge(i, i - (width + 1), weight=weight)
            i += 1
    print(f"Graph created with {len(G.nodes)} nodes and {len(G.edges)} edges")
    return G



