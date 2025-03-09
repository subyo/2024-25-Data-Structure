class Example:
    def __init__(self):
        self.data = [1, 2, 3]  # Örnek bir veri listesi
        self.numItems = len(self.data)  # Veri listesinin eleman sayısı

    def __repr__(self):
        s = "Example(["
        for i in range(self.numItems):
            s = s + repr(self.data[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s

# Example sınıfından bir örnek oluşturup resmi temsilini yazdıralım
example_instance = Example()
print(repr(example_instance)) 