from collections import deque

def build_graph():
    graph = {
        0: [1, 10], 1: [0, 4], 2: [3], 3: [2, 6, 9], 4: [1, 5],
        5: [4, 7], 6: [3], 7: [5, 12], 8: [2], 9: [3, 10, 17],
        10: [0, 9, 11], 11: [10, 12], 12: [7, 11], 13: [14], 14: [13, 15],
        15: [14, 16, 17], 16: [15], 17: [9, 15, 18, 23, 24], 18: [17, 19],
        19: [18, 20], 20: [19, 21], 21: [20, 22, 28], 22: [21],
        23: [17, 24], 24: [17, 23, 25], 25: [24, 26], 26: [25],
        27: [24, 28, 29], 28: [21, 27, 29], 29: [27, 28]
    }
    return graph

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == end:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path.copy())
            if new_path:
                return new_path
    return None

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

graph = build_graph()
dfs_path = dfs(graph, 9, 29)
bfs_path = bfs(graph, 9, 29)

print(f"DFS Path from 9 to 29: {dfs_path}")
print(f"BFS Shortest Path from 9 to 29: {bfs_path}")
