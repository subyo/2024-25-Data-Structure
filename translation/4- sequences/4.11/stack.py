class Stack:
    def __init__(self):
        self.items = []
    
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Boş yığının üst elemanını almak denemesi")
        
        topldx = len(self.items) - 1
        item = self.items[topldx]
        del self.items[topldx]
        return item
    
    def push(self, item):
        self.items.append(item)
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Boş yığının üst elemanını almak denemesi")
        
        topldx = len(self.items) - 1
        return self.items[topldx]
    
    def isEmpty(self):
        return len(self.items) == 0

def main():
    s = Stack()
    lst = list(range(10))
    lst2 = []
    
    for k in lst:
        s.push(k)
        
    if s.top() == 9:
        print("Test 1 Başarılı")
    else:
        print("Test 1 Başarısız")
        
    while not s.isEmpty():
        lst2.append(s.pop())
        
    lst2.reverse()
    
    if lst2 !=lst:
        print("Test 2 Başarısız")
    else:
        print("Test 2 Başarılı")
    try:
        s.pop()
        print("Test 3 Başarısız")
        
    except RuntimeError:
        print("Test 3 Başarılı")
    except:
        print("Test 3 Başarısız")

    try:
        s.top()
        print("Test 4 Başarısız")
        
    except RuntimeError:
        print("Test 4 Başarılı")
    except:
        print("Test 4 Başarısız")

if __name__ == "__main__":
    main()
    
# Bu kod, bir yığın (stack) veri yapısının temel işlevlerini gerçekleştiren bir Python sınıfı tanımlar. 
# Yığın, verilerin son giren ilk çıkar (LIFO - Last In, First Out) prensibiyle saklandığı bir veri yapısıdır. 
# Kodun içindeki Stack sınıfı, yığın işlemleri için push, pop, top, ve isEmpty gibi metodları içerir. 
# Ayrıca, main fonksiyonu bu metodların doğru çalıştığını test eden bir dizi test içerir. 