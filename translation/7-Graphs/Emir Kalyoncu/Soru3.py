import heapq

class Graph:
    def __init__(self, num_vertices):
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.num_vertices
        dist[src] = 0
        pq = [(dist[src], src)]
        visited = set()

        while pq:
            u, _ = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)

            for neighbor, weight in self.graph[u]:
                if neighbor not in visited:
                    new_dist = dist[u] + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

        return dist

# Assuming you have extracted the graph data from the image (adjacency matrix or edge list format)
# Replace the following lines with your data
graph = Graph(29)  # Assuming 29 vertices based on the image
graph.add_edge(0, 1, 4.64)
graph.add_edge(0, 2, 5.53)
# ... (all other edges)
graph.add_edge(27, 28, 4.24)

# Perform Dijkstra's algorithm from vertex 9
dist = graph.dijkstra(9)

# Print the minimum cost to visit all other vertices
for i in range(len(dist)):
    if i != 9:
        print(f"Minimum cost to visit vertex {i} from vertex 9: {dist[i]}")
