1.Yığın sıralama algoritmasının 2. versiyonunu uygulayın. İki sıralama algoritmasının 
(yığın sıralama ve hızlı sıralama) yürütme sürelerini karşılaştırmak için kendi testlerinizi kullanın.
 Verilerinizi plot formatında çıktı olarak verin ve metin web sitesinde sağlanan PlotData.py programını kullanarak verilerinizi çizin.
import time
import random
import matplotlib.pyplot as plt

def yiginsiralama_v2(dizi):
    n = len(dizi)

    # Maksimum yığını oluştur.
    for i in range(n // 2 - 1, -1, -1):
        yiginlastir(dizi, n, i)

    # Yığından tek tek elemanları çıkar.
    for i in range(n - 1, 0, -1):
        dizi[i], dizi[0] = dizi[0], dizi[i]  # Takas
        yiginlastir(dizi, i, 0)

def yiginlastir(dizi, n, i):
    en_buyuk = i  # En büyüğü kök olarak başlat.
    sol = 2 * i + 1     # Sol = 2*i + 1
    sag = 2 * i + 2     # Sağ = 2*i + 2

    # Kökün sol çocuğu varsa ve kökten büyükse.
    if sol < n and dizi[en_buyuk] < dizi[sol]:
        en_buyuk = sol

    # Kökün sağ çocuğu varsa ve kökten büyükse.
    if sag < n and dizi[en_buyuk] < dizi[sag]:
        en_buyuk = sag

    # Kök değiştiyse.
    if en_buyuk != i:
        dizi[i], dizi[en_buyuk] = dizi[en_buyuk], dizi[i]  # Takas

        # Kökü yığınlaştır.
        yiginlastir(dizi, n, en_buyuk)

def hizlisiralama(dizi):
    def partition(low, high):
        i = (low - 1)         # Küçük elemanın indeksi.
        pivot = dizi[high]     # Pivot.

        for j in range(low, high):

            # Eğer mevcut eleman pivottan küçük veya eşitse.
            if dizi[j] <= pivot:

                # Küçük elemanın indeksini artır.
                i = i + 1
                dizi[i], dizi[j] = dizi[j], dizi[i]

        dizi[i + 1], dizi[high] = dizi[high], dizi[i + 1]
        return (i + 1)

    def quicksort_recursive(low, high):
        if low < high:

            # pi bölümlendirme indeksi, dizi[pi] artık doğru yerde.
            pi = partition(low, high)

            # Bölümlemeden önce ve sonraki elemanları ayrı ayrı sırala.
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)
    
    quicksort_recursive(0, len(dizi)-1)


# Test et ve yürütme sürelerini karşılaştır.
boyutlar = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]  # Daha iyi karşılaştırma için artırılmış boyutlar.
yigin_sureleri = []
hizli_sureler = []

for boyut in boyutlar:
    dizi1 = [random.randint(0, boyut) for _ in range(boyut)]  # Rastgele dizi oluştur.
    dizi2 = dizi1[:]  # Hızlı sıralama için diziyi kopyala.

    baslangic_zamani = time.time()
    yiginsiralama_v2(dizi1)
    bitis_zamani = time.time()
    yigin_sureleri.append(bitis_zamani - baslangic_zamani)

    baslangic_zamani = time.time()
    hizlisiralama(dizi2)
    bitis_zamani = time.time()
    hizli_sureler.append(bitis_zamani - baslangic_zamani)

# Verileri çizme.
plt.plot(boyutlar, yigin_sureleri, label="Yığın Sıralama V2")
plt.plot(boyutlar, hizli_sureler, label="Hızlı Sıralama")
plt.xlabel("Dizi Boyutu")
plt.ylabel("Yürütme Süresi (saniye)")
plt.title("Yığın Sıralama vs. Hızlı Sıralama Performansı")
plt.legend()
plt.grid(True)
plt.xscale("log")  # x ekseni için logaritmik ölçek kullan.
plt.yscale("log")  # y ekseni için logaritmik ölçek kullan.
plt.show()

# Verileri plot formatında kaydet (istendiği gibi).
with open("siralama_verileri.txt", "w") as f:
    f.write("Boyut\tYığın Sıralama\tHızlı Sıralama\n")
    for i in range(len(boyutlar)):
        f.write(f"{boyutlar[i]}\t{yigin_sureleri[i]}\t{hizli_sureler[i]}\n")

print("Veriler siralama_verileri.txt dosyasına kaydedildi.")
