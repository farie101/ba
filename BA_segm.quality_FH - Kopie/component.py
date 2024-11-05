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

        # Get the components before union
        comp_u = self.S[u_rep]
        comp_v = self.S[v_rep]

        # Determine which component is larger
        size_u = len(comp_u.nodes)
        size_v = len(comp_v.nodes)

        self.mst.append(edge)
        self.max_edge_in_mst = edge

        # Perform union
        new_rep = self.unionfind.union(u, v)

        # Merge smaller component into larger one
        if size_u >= size_v:
            larger_comp = comp_u
            smaller_comp = comp_v
        else:
            larger_comp = comp_v
            smaller_comp = comp_u

        # Update the component map with the new representative
        self.S[new_rep] = larger_comp
        larger_comp.merge(smaller_comp)

    def merge(self, smaller_comp):
        """
        Merge smaller component into this one
        """
        # Update nodes and MST
        self.nodes.update(smaller_comp.nodes)
        self.mst.extend(smaller_comp.mst)

        # Delete the smaller component from S
        self.__delete__(smaller_comp)

       # print(f"After merge - Representative: {self.representative}, Nodes: {self.nodes}")

    def get_max_edge_weight(self):
        if self.max_edge_in_mst:
            u, v = self.max_edge_in_mst
            return self.graph[u][v]['weight']
        return 0



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