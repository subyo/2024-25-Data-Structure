import timeit
import xml.etree.ElementTree as ET
import random

# ✅ Daha iyi çalışan toplama fonksiyonu
def toplam(liste):
    """
    Verilen bir listedeki tüm değerleri toplar ve toplamı döndürür.
    """
    toplam = 0
    for sayi in liste:
        toplam += sayi
    return toplam

# ✅ Daha verimli test verisi oluşturma
liste_boyutlari = [100, 1000, 10000, 100000, 1000000] 
listeler = [[random.randint(1, 100) for _ in range(boyut)] for boyut in liste_boyutlari]

# ✅ Daha hassas zaman ölçme
zamanlar = []
for liste in listeler:
    zaman = timeit.timeit(lambda: toplam(liste), number=10) / 10  # 10 kez çalıştırıp ortalama al
    zamanlar.append(zaman)

# ✅ XML formatını düzeltme
kok = ET.Element("ExperimentalResults")  

for boyut, zaman in zip(liste_boyutlari, zamanlar):
    eleman = ET.SubElement(kok, "Comparison")
    ET.SubElement(eleman, "Size").text = str(boyut)
    ET.SubElement(eleman, "Time").text = str(zaman)

# ✅ XML dosyasını doğru kaydetme
xml_data = ET.tostring(kok, encoding="utf-8").decode()
with open("toplam_sureleri.xml", "w", encoding="utf-8") as f:
    f.write(xml_data)

print("✅ XML dosyası 'toplam_sureleri.xml' başarıyla oluşturuldu!")
