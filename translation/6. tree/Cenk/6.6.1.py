def dfs(current, goal, graph, visited=None):
    if visited is None:
        visited = set()

    visited.add(current)

    if current == goal:
        return [current]

    for next_node in graph[current]:
        if next_node not in visited:
            result = dfs(next_node, goal, graph, visited)
            if result is not None:
                return [current] + result

    return None

# Graf yapısını oluşturalım
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E'],
    'C': ['A'],
    'D': ['E'],
    'E': ['B', 'D']
}

# Örnek uygulama: 'A' düğümünden 'D' düğümüne bir yol arayalım
start_node = 'A'
goal_node = 'D'
path = dfs(start_node, goal_node, graph)

# Sonucu yazdıralım
if path is not None:
    print(f"Bir yol bulundu: {' -> '.join(path)}")
else:
    print("Belirlenen düğümler arasında bir yol bulunamadı.")
