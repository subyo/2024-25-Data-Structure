import time
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def yerDegistir(text):
    if len(text) <= 1:
        return text
    return text[1] + text[0] + yerDegistir(text[2:])

def performansTesti():
    test_metinler = [str(i) for i in range(1, 11)]  # 1-10 arası sayılar
    zamanlar = []

    for metin in test_metinler:
        baslangic_zamani = time.time()
        _ = yerDegistir(metin)
        bitis_zamani = time.time()
        zamanlar.append(bitis_zamani - baslangic_zamani)

    return test_metinler, zamanlar

def xmlOlustur(test_metinler, zamanlar):
    root = ET.Element("PerformansVerileri")
    
    for metin, zaman in zip(test_metinler, zamanlar):
        entry = ET.SubElement(root, "TestEntry")
        ET.SubElement(entry, "Metin").text = metin
        ET.SubElement(entry, "Zaman").text = str(zaman)

    tree = ET.ElementTree(root)
    tree.write("performans_verileri.xml")

def plotGorsellestir(test_metinler, zamanlar):
    plt.plot(test_metinler, zamanlar, marker='o')
    plt.title('Ters Çevirme İşleminin Performansı')
    plt.xlabel('Metin Uzunluğu')
    plt.ylabel('Geçen Zaman (saniye)')
    plt.show()

# Performans testi yap
test_metinler, zamanlar = performansTesti()

# Performans verilerini XML dosyasına yaz
xmlOlustur(test_metinler, zamanlar)

# Performansı görselleştir
plotGorsellestir(test_metinler, zamanlar)
