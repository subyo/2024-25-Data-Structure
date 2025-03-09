class Edge:
    def __init__(self, v1, v2, weight=0):  # Yapıcı metod (constructor)
        self.v1 = v1  # İlk düğüm
        self.v2 = v2  # İkinci düğüm
        self.weight = weight  # Kenar ağırlığı
    
    def __lt__(self, other):
        """Kenarları ağırlıklarına göre karşılaştırır."""
        return self.weight < other.weight
    
    def __repr__(self):
        """Kenar bilgilerini okunaklı şekilde döndürür."""
        return f"Edge({self.v1}, {self.v2}, {self.weight})"

# Örnek bir Edge nesnesi oluşturup ekrana yazdıralım
edge1 = Edge("A", "B", 5)
print(edge1)  # Çıktıyı görmek için print() fonksiyonunu kullanmalısın
