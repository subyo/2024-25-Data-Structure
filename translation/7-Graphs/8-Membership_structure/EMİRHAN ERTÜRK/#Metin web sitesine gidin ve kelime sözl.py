#Metin web sitesine gidin ve kelime sözlüğünü indirin. Bu kelime listesi için bir bloom filtresi oluşturun ve bağımsızlık bildirgesini yazım denetimi yapmak için kullanın, yanlış yazılan tüm kelimeleri ekrana yazdırın 

import hashlib 

  

class BloomFilter: 

    def __init__(self, size, hash_count): 

        self.size = size 

        self.hash_count = hash_count 

        self.bits = [0] * size 

  

    def add(self, item): 

        for i in range(self.hash_count): 

            hash_index = hash_function(item, i, self.size) 

            self.bits[hash_index] = 1 

  

    def check(self, item): 

        for i in range(self.hash_count): 

            hash_index = hash_function(item, i, self.size) 

            if self.bits[hash_index] == 0: 

                return False 

        return True 

  

def hash_function(item, index, size): 

    return (hash(item) + index * hash(str(item)) % size) % size 

  

# Örnek kelime listesi 

kelime_listesi = ["merhaba", "selam", "nasılsın", "compter", "keyboard"] 

  

# Bloom filtresi oluşturma 

bloom_filter = BloomFilter(100, 5) 

  

# Kelime listesini Bloom filtresine ekleme 

for kelime in kelime_listesi: 

    bloom_filter.add(kelime) 

  

# Yanlış yazılan kelimeleri kontrol etme 

for kelime in ["compter", "keyboards", "mouse"]: 

    if not bloom_filter.check(kelime): 

        print(f"{kelime} yanlış yazılmıştır.") 