import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        curr_dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Örnek Kullanım:
graph = {
    9: [(10, 4), (12, 2)],
    10: [(15, 5)],
    15: [(29, 6)],
    12: [(29, 3)]
}

distances = dijkstra(graph, 9)
print("Minimum costs:", distances)
