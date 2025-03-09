import time 

import random 

import string 

 

 

def string_karsilastirma(str1, str2): 

    start_time = time.time_ns()      # Fonksiyonun başlangıcındaki zamanı al 

    result = str1 == str2           # İki stringi karşılaştır 

    end_time = time.time_ns()      # Fonksiyonun sonundaki zamanı al 

    return end_time - start_time  # Geçen süreyi döndür 

 

 

uzunluk = 100  # Oluşturulacak stringlerin uzunluğunu belirle 

 

 

 

# random.choices() fonksiyonu, belirtilen uzunlukta rastgele karakterler seçer. string.#ascii_lowercase küçük harfleri içeren bir string, 

# string.ascii_uppercase ise büyük harfleri içeren bir string döndürür. 

 

 

str1 = ''.join(random.choices(string.ascii_lowercase, k=uzunluk)) 

str2 = ''.join(random.choices(string.ascii_uppercase, k=uzunluk))  

 

 

 

sure = string_karsilastirma(str1, str2)  # Karşılaştırma işlemi için süreyi hesapla 

 

# Sonucu göster 

print("String Uzunluğu:", uzunluk) 

print("Karşılaştırma Süresi (nanosaniye):", sure) 