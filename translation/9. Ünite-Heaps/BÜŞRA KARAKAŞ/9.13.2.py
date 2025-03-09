import time
import random
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def yiginsiralama_v1(dizi):  # Version 1 (Klasik Yığın Sıralama)
    n = len(dizi)

    for i in range(n // 2 - 1, -1, -1):
        yiginlastir_v1(dizi, n, i)

    for i in range(n - 1, 0, -1):
        dizi[i], dizi[0] = dizi[0], dizi[i]
        yiginlastir_v1(dizi, i, 0)

def yiginlastir_v1(dizi, n, i):
    en_buyuk = i
    sol = 2 * i + 1
    sag = 2 * i + 2

    if sol < n and dizi[en_buyuk] < dizi[sol]:
        en_buyuk = sol

    if sag < n and dizi[en_buyuk] < dizi[sag]:
        en_buyuk = sag

    if en_buyuk != i:
        dizi[i], dizi[en_buyuk] = dizi[en_buyuk], dizi[i]
        yiginlastir_v1(dizi, n, en_buyuk)

def yiginsiralama_v2(dizi):  # Version 2 (Aşağıdan Yukarıya Yığın Oluşturma)
    n = len(dizi)

    for i in range(n // 2 - 1, -1, -1):
        yiginlastir_v2(dizi, n, i)

    for i in range(n - 1, 0, -1):
        dizi[i], dizi[0] = dizi[0], dizi[i]
        yiginlastir_v2(dizi, i, 0)

def yiginlastir_v2(dizi, n, i):
    en_buyuk = i
    sol = 2 * i + 1
    sag = 2 * i + 2

    if sol < n and dizi[en_buyuk] < dizi[sol]:
        en_buyuk = sol

    if sag < n and dizi[en_buyuk] < dizi[sag]:
        en_buyuk = sag

    if en_buyuk != i:
        dizi[i], dizi[en_buyuk] = dizi[en_buyuk], dizi[i]
        yiginlastir_v2(dizi, n, en_buyuk)

# Test ve Karşılaştırma
boyutlar = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
veriler = []

for boyut in boyutlar:
    dizi1 = [random.randint(0, boyut) for _ in range(boyut)]
    dizi2 = dizi1[:]  # Kopyasını al

    baslangic_zamani = time.time()
    yiginsiralama_v1(dizi1)
    bitis_zamani = time.time()
    sure_v1 = bitis_zamani - baslangic_zamani

    baslangic_zamani = time.time()
    yiginsiralama_v2(dizi2)
    bitis_zamani = time.time()
    sure_v2 = bitis_zamani - baslangic_zamani

    veriler.append({"boyut": boyut, "sure_v1": sure_v1, "sure_v2": sure_v2})

# XML Oluşturma
kok = ET.Element("data")
for veri in veriler:
    test = ET.SubElement(kok, "test")
    boyut = ET.SubElement(test, "size")
    boyut.text = str(veri["boyut"])
    zaman_v1 = ET.SubElement(test, "version1")
    zaman_v1.text = str(veri["sure_v1"])
    zaman_v2 = ET.SubElement(test, "version2")
    zaman_v2.text = str(veri["sure_v2"])

agac = ET.ElementTree(kok)
agac.write("yigin_siralama_karsilastirma.xml")

# Verileri Çizme (Matplotlib ile)
boyutlar = [veri["boyut"] for veri in veriler]
sure_v1 = [veri["sure_v1"] for veri in veriler]
sure_v2 = [veri["sure_v2"] for veri in veriler]

plt.plot(boyutlar, sure_v1, label="Yığın Sıralama V1")
plt.plot(boyutlar, sure_v2, label="Yığın Sıralama V2")
plt.xlabel("Dizi Boyutu")
plt.ylabel("Yürütme Süresi (saniye)")
plt.title("Yığın Sıralama V1 vs. V2 Performansı")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.yscale("log")
plt.show()

print("Veriler yigin_siralama_karsilastirma.xml dosyasına kaydedildi.")
