import time 
from lxml import etree as ET 
import matplotlib.pyplot as plt 

def compare_numbers(num1, num2): 
    if num1 < num2: 
        return -1 
    elif num1 == num2: 
        return 0 
    else: 
        return 1 

def experimental_data(start, end): 
    data = [] 
    for i in range(start, end): 
        start_time = time.time() 
        compare_numbers(i, i+1) 
        end_time = time.time() 
        elapsed_time = end_time - start_time 
        data.append((i, elapsed_time)) 
    return data 

def write_xml(data, filename): 
    root = ET.Element("ExperimentalResults") 
    for item in data: 
        element = ET.SubElement(root, "Comparison") 
        ET.SubElement(element, "Number").text = str(item[0]) 
        ET.SubElement(element, "Time").text = str(item[1]) 

    tree = ET.ElementTree(root) 
    tree.write(filename, pretty_print=True) 

def plot_results(data): 
    numbers = [item[0] for item in data] 
    times = [item[1] for item in data] 
     
    plt.plot(numbers, times) 
    plt.xlabel('Numbers') 
    plt.ylabel('Time (s)') 
    plt.title('Experimental Comparison Times') 
    plt.show() 

# Örnek kullanım 
start = 1 
end = 10000 
experimental_results = experimental_data(start, end) 
print(experimental_results) 

# XML dosyası oluşturma 
write_xml(experimental_results, 'experimental_results.xml') 

# Sonuçları çizimleyerek görselleştirme 
plot_results(experimental_results) 
