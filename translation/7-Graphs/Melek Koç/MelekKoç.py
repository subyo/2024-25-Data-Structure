def is_bipartite(graph):
    color = {}
    
    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(nei, c ^ 1) for nei in graph[node])
    
    return all(dfs(node, 0) for node in graph if node not in color)

# Örnek kullanım
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

if is_bipartite(graph):
    print("Evet, iki parçalıdır.")
else:
    print("Hayır, iki parçalı değildir.")