from component import  Component
def Int(C: Component):
    return C.get_max_edge_weight()
def Tau(k,C: Component):
    return k / len(C.nodes)
def MInt(C1, C2, k):
    return min(Int(C1) + Tau(k, C1), Int(C2)+Tau(k, C2))
