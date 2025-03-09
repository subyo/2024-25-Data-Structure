from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])  # Başlangıç noktası ve yolu tutan kuyruk
    visited = set()

    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))
    return None

# Örnek Kullanım:
graph = {
    9: [10, 12],
    10: [15],
    15: [29],
    12: [29]  # gibi kenarları ekleyin
}

path = bfs_shortest_path(graph, 9, 29)
print("Shortest Path:", path)
