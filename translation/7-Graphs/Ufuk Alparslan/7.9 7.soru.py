from collections import deque

def is_bipartite_and_get_sets(graph):
    color = {}  # Düğümleri boyamak için bir sözlük
    set1, set2 = set(), set()
    
    for start in graph:  # Graf birden fazla bileşenden oluşabilir, her düğümü kontrol et
        if start not in color:
            queue = deque([start])
            color[start] = 0
            set1.add(start)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]  # Farklı renk ata
                        queue.append(neighbor)
                        if color[neighbor] == 0:
                            set1.add(neighbor)
                        else:
                            set2.add(neighbor)
                    elif color[neighbor] == color[node]:
                        return "No, it is not bipartite"

    return f"Yes, it is bipartite\nSet 1: {set1}\nSet 2: {set2}"

# Örnek Kullanım:
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
    4: [5],  # Bağımsız bileşen ekledik
    5: [4]
}

print(is_bipartite_and_get_sets(graph))
