class Component:
    def __init__(self, node, unionfind, S, graph):
        self.nodes = {node}
        self.representative = node
        self.mst = []
        self.max_edge_in_mst = None
        self.unionfind = unionfind
        self.S = S
        self.graph =graph

        S[node] = self

    def add_edge(self, edge):
        u, v = edge
        if u == v:
            raise ValueError(f"Self-loop detected: {u} -> {v} is not allowed.")

        u_rep = self.unionfind.find(u)
        v_rep = self.unionfind.find(v)

        if u_rep == v_rep:
            raise ValueError(f"Both {u} and {v} are already in the same component.")

        if u_rep != self.representative and v_rep != self.representative:
            raise ValueError(f"Neither of {u} and {v} are in the component.")

        if u_rep == self.representative:
            other_node = v
        else:
            other_node = u

        self.mst.append(edge)
        self.max_edge_in_mst = edge

        other_rep = self.unionfind.find(other_node)
        other_component = self.S[other_rep]
        self.unionfind.union(u, v)
        self.merge(other_component)



        print(f"Inhalt von S nach Hinzufügen der Kante {u}-{v}: {[k for k in self.S.keys()]}")
        print(f"Union-Find Eltern: {self.unionfind.parent}")



    def get_max_edge_weight(self):
        if self.max_edge_in_mst:
            u, v = self.max_edge_in_mst
            return self.graph[u][v]['weight']
        return 0

    def merge(self, C2):

        # Ensure self is the larger component by swapping if necessary
        if len(self.nodes) < len(C2.nodes):
            self, C2 = C2, self

        # Update self to include all nodes and edges from C2
        self.nodes.update(C2.nodes)
        self.mst.extend(C2.mst)
        self.__delete__(C2)

    def __delete__(self, C2):
        # Remove C2's representative entry from S if it exists
        if C2.representative in self.S:
            del self.S[C2.representative]

        # Clear all attributes of C2 to prevent further use
        C2.nodes = set()
        C2.mst = []
        C2.representative = None
        C2.max_edge_in_mst = None
    def __eq__(self, other):
        if not isinstance(other, Component):
            return False
        return self.nodes == other.nodes

    def get_mst(self):
        return self.mst

    def get_nodes(self):
        return self.nodes