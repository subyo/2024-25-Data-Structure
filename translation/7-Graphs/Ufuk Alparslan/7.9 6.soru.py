def is_bipartite(graph, start):
    color = {}
    queue = [start]
    color[start] = 0

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in color:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return "No, it is not bipartite"
    return "Yes, it is bipartite"

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(is_bipartite(graph, 0))
