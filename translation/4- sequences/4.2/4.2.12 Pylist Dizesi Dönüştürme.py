class Example:
    def __init__(self):
        self.data = [1, 2, 3]  # Örnek bir veri listesi
        self.numItems = len(self.data)  # Veri listesinin eleman sayısı

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + repr(self.data[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s

# Example sınıfından bir örnek oluşturup string temsilini yazdıralım
example_instance = Example()
print(str(example_instance)) 