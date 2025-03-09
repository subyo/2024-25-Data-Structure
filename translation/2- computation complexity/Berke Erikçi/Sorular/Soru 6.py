import random
import time
import xml.etree.ElementTree as ET

class Clearable:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size  # Sabit boyutlu liste
        self.count = 0

    def append(self, item):
        if self.count == self.size:
            self.items = [None] * self.size  # Listeyi temizleme
            self.count = 0
        self.items[self.count] = item
        self.count += 1

    def __getitem__(self, index):
        if 0 <= index < self.count:
            return self.items[index]
        return None

def run_experiment(sizes, append_counts):
    results = {}
    
    for size in sizes:
        for append_count in append_counts:
            times = []
            for _ in range(10):  # Ortalama almak için 10 kez çalıştırıyoruz
                cl = Clearable(size)
                start = time.time()
                for _ in range(append_count):
                    cl.append(random.randint(0, 1000))
                end = time.time()
                times.append(end - start)
            results[(size, append_count)] = sum(times) / len(times)  # Ortalama süre
    
    return results

def save_results_to_xml(results, filename):
    root = ET.Element('ExperimentalResults')
    
    for (size, append_count), avg_time in results.items():
        entry = ET.SubElement(root, 'Experiment')
        ET.SubElement(entry, 'Size').text = str(size)
        ET.SubElement(entry, 'AppendCount').text = str(append_count)
        ET.SubElement(entry, 'AvgTime').text = str(avg_time)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def main():
    sizes = [10, 100, 1000]
    append_counts = [100, 1000, 10000]
    
    results = run_experiment(sizes, append_counts)
    save_results_to_xml(results, 'clearable_experiment_results.xml')
    
    for (size, append_count), avg_time in results.items():
        print(f"Boyut: {size}, Append Sayısı: {append_count}, Ortalama Süre: {avg_time:.6f} saniye")

if __name__ == "__main__":
    main()