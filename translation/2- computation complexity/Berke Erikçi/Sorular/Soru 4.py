import time
import xml.etree.ElementTree as ET

def arama(liste, deger):
    """Doğrusal arama fonksiyonu. Değeri bulursa indeksini döndürür, bulamazsa -1 döndürür."""
    for i, val in enumerate(liste):  # Daha verimli bir döngü
        if val == deger:
            return i
    return -1

def zamanlama_testi():
    """Farklı liste boyutlarında arama süresini ölçer ve sonuçları bir XML dosyasına kaydeder."""
    list_sizes = [100, 1_000, 10_000, 100_000, 500_000]  # Farklı boyutlar için test
    results = {}

    for size in list_sizes:
        liste = list(range(size))  # 0'dan size-1'e kadar sayı içeren liste
        deger = liste[size // 2]   # Listenin ortasındaki elemanı arıyoruz

        # Kendi yazdığımız arama fonksiyonunun süresi
        start_time = time.perf_counter()
        arama(liste, deger)
        end_time = time.perf_counter()
        elapsed_time_manual = end_time - start_time

        # Python'un list.index() metodunun süresi
        start_time = time.perf_counter()
        liste.index(deger)  # index() metodu kullanımı
        end_time = time.perf_counter()
        elapsed_time_builtin = end_time - start_time

        results[size] = (elapsed_time_manual, elapsed_time_builtin)
        print(f"Liste Boyutu: {size}, Manuel Arama Süresi: {elapsed_time_manual:.8f} s, index() Süresi: {elapsed_time_builtin:.8f} s")

    # XML'e kaydetme
    write_xml(results, "search_results.xml")
    print("Sonuçlar XML dosyasına kaydedildi: search_results.xml")

def write_xml(results, filename):
    """Sonuçları XML formatında dosyaya kaydeder."""
    root = ET.Element("Ploy")

    for size, times in results.items():
        entry = ET.SubElement(root, "DataPoint")
        ET.SubElement(entry, "ListSize").text = str(size)
        ET.SubElement(entry, "ManualSearchTime").text = str(times[0])
        ET.SubElement(entry, "BuiltinSearchTime").text = str(times[1])

    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        tree.write(xml_file)

# Testi çalıştır
zamanlama_testi()
