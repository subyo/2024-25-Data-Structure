import time 

 

def carpma_suresi(x, y): 

    start_time = time.time_ns() 

    x * y 

    end_time = time.time_ns() 

    return end_time - start_time 

 

# İki farklı boyuttaki sayıları belirle 

x1 = 5 

y1 = 7 

x2 = 92342121 

y2 = 56782122 

 

# İki farklı boyuttaki sayıları çarpma işlemi için süreyi ölç 

sure1 = carpma_suresi(x1, y1) 

sure2 = carpma_suresi(x2, y2) 

 

# Sonuçları göster 

print("1. Boyuttaki Sayılar Çarpma Süresi:", sure1, "mikrosaniye") 

print("2. Boyuttaki Sayılar Çarpma Süresi:", sure2, "mikrosaniye") 