from component import  Component
def Int(C: Component):
    return C.get_max_edge_weight()

def Tau(k,C: Component):
    return k / len(C.nodes)
def MInt(C1, C2, k):

    print(f"MST von {C1.representative}: {C1.mst()}")
    print(f"Int von {C1.representative}: {Int(C1)}")
    print(f"MST von {C2.representative}: { C2.get_max_edge_weight()}")
    print(f"Int von {C2.representative}: {Int(C2)}")

    return min(Int(C1) + Tau(k, C1), Int(C2)+Tau(k, C2))
