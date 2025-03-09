class Example:
    def __init__(self):
        self.items = [1, 2, 3]  # Örnek bir veri listesi
        self.numItems = len(self.items)  # Veri listesinin eleman sayısı

    def __contains__(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        return False

# Example sınıfından bir örnek oluştur
example_instance = Example()

# Örneğin içinde belirli bir öğenin bulunup bulunmadığını kontrol et
result = 2 in example_instance
print(result) 