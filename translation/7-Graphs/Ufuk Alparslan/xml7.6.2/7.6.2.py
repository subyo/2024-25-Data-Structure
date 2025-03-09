class Vertex:
    def __init__(self, vertexId, x, y, label):  # Yapıcı metod
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None

    def __repr__(self):
        return f"Vertex({self.vertexId}, {self.x}, {self.y}, '{self.label}')"

# Örnek bir Vertex nesnesi oluşturup ekrana yazdıralım
vertex1 = Vertex(1, 10, 20, "A")
print(vertex1)  # Çıktı almak için print() fonksiyonunu kullanmalısın
