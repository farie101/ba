class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Always make the root of the larger tree the parent
            if self.size[root_u] >= self.size[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            else:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]

    def connected(self, v, u):
        return self.find(v) == self.find(u)

    def get_size(self, u):
        return self.size[self.find(u)]

