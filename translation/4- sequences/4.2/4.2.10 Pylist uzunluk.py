class SimpleList:
    def __init__(self, data):
        self.items = data
        self.numItems = len(self.items)
    
    def __len__(self):
        return self.numItems

# SimpleList sınıfından bir örnek oluştur
my_list = SimpleList([10, 20, 30, 40])

# Oluşturulan listeyi kullanarak uzunluğunu elde et
length = len(my_list)

print(f"Liste Uzunluğu: {length}")