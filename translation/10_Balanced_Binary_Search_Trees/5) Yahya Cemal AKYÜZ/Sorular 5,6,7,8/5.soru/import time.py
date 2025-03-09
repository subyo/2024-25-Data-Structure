import time
import random
import xml.etree.ElementTree as ET

def measure_list_access_time(sizes):
    results = []
    for size in sizes:
        test_list = list(range(size))  # 0'dan size'a kadar bir liste oluştur
        random_indices = [random.randint(0, size - 1) for _ in range(1000)]  # 1000 rastgele indeks seç
        
        start_time = time.time()
        for index in random_indices:
            _ = test_list[index]  # Listeye erişim
        end_time = time.time()
        
        access_time = (end_time - start_time) * 1e6  # Mikro saniye cinsine çevir
        results.append((size, access_time))
    return results

def generate_xml(data, filename="ListAccessTiming.xml"):
    root = ET.Element("Plot", title="Average List Element Access Time")
    axes = ET.SubElement(root, "Axes")
    ET.SubElement(axes, "XAxis", min=str(data[0][0]), max=str(data[-1][0])).text = "List Size"
    ET.SubElement(axes, "YAxis", min="0", max=str(max(d[1] for d in data))).text = "Microseconds"
    
    sequence = ET.SubElement(root, "Sequence", title="List Access Time", color="blue")
    for size, time_taken in data:
        ET.SubElement(sequence, "DataPoint", type="I", x=str(size), y=str(time_taken))
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def main():
    sizes = [100, 10100, 20100, 30100, 40100, 50100, 60100, 70100, 80100, 90100]
    results = measure_list_access_time(sizes)
    generate_xml(results)
    print("List access timing data saved to ListAccessTiming.xml")

if __name__ == "__main__":
    main()
