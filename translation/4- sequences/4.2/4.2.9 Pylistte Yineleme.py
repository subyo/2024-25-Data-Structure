class SimpleIterator:
    def __init__(self, data):
        self.items = data
        self.numItems = len(self.items)
    
    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

# SimpleIterator sınıfından bir örnek oluştur
my_iterator = SimpleIterator([10, 20, 30])

# Oluşturulan iterator üzerinde döngü yap
for item in my_iterator:
    print(item)