class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        self.edges.sort()
        parent, rank = {}, {}
        for node in range(self.V):
            parent[node] = node
            rank[node] = 0
        mst = []
        for edge in self.edges:
            w, u, v = edge
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append(edge)
        return mst

# Örnek Kullanım:
g = Graph(6)
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal()
print("Minimum Spanning Tree:", mst)
