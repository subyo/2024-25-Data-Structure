from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, target, path=[]):
        path = path + [start]
        if start == target:
            return path
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.dfs(neighbor, target, path)
                if new_path:
                    return new_path
        return None

# Örnek Kullanım:
g = Graph()
g.add_edge(9, 10)
g.add_edge(10, 15)
g.add_edge(15, 29)  # gibi kenarları ekleyin

path = g.dfs(9, 29)
print("Path:", path)
