class MyList:
    def __init__(self):
        self.items = []
        self.numItems = 0

    def add(self, item):
        self.items.append(item)
        self.numItems += 1

    def __delitem__(self, index):
        # Direkt olarak 'del' komutu ile elemanı siliyoruz.
        del self.items[index]
        self.numItems -= 1

    def __str__(self):
        # Listenin bir temsilini döndürür
        return str(self.items)

# MyList sınıfından bir örnek oluştur
my_list = MyList()

# Listeye bazı öğeler ekleyelim
my_list.add('a')
my_list.add('b')
my_list.add('c')

# Belirli bir indeksteki öğeyi silelim (b'yi, yani indeks 1 olan öğeyi silelim)
del my_list[1]

# Listenin güncellenmiş halini yazdıralım
print(my_list)  # ['a', 'c']
print(my_list.numItems) 