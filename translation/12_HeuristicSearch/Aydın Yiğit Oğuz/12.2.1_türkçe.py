def graphDFS(G, start, goal):
    # G = (V,E) grafı, düğümler (V) ve kenarlardan (E) oluşur.
    V, E = G
    stack = Stack()
    visited = Set()
    stack.push([start]) # Yığın, yolları içeren bir yığındır.

    while not stack.isEmpty():
        # Yığından bir yol çıkarılır.
        path = stack.pop()
        current = path[0] # Yolun son düğümü alınır.
        if not current in visited:
            # Mevcut düğüm ziyaret edilenler kümesine eklenir.
            visited.add(current)

            # Eğer mevcut düğüm hedef düğümse, arama durdurulur ve hedefe giden yol döndürülür.
            if current == goal:
                return path # Hedefe giden yolu döndür.

            # Aksi takdirde, mevcut düğüme komşu olan her düğüm için:
            # - Eğer düğüm zaten yolda yoksa, yeni yol yığına eklenir.
            # - Eğer düğüm zaten yolda varsa, bu kenar göz ardı edilir.
            for v in adjacent(current, E):
                if not v in path:
                    stack.push([v] + path)

    # Eğer buraya kadar geldiysek, hedef bulunamadı.
    return [] # Boş bir yol döndür.
