class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0
    def __compress(self):
        newlst = []
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])
            
        self.items = newlst
        self.frontIdx = 0
        
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Boş bir sırayı iptal etme girişimi")
        
        if self.frontIdx*2> len(self.items):
            self.__compress()
            
        item = self.items[self.frontIdx]
        self.frontIdx +=1
        return item
    
    def enqueue(self, item):
        self.items.append(item)
        
    def front (self):
        if self.isEmpty():
            raise RuntimeError("Boş sıranın önüne erişmeye çalış")
        
        return self.items[self.frontIdx]
    
    def isEmpty(self):
        return self.frontIdx == len(self.items)
    
def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []
        
    for k in lst:
        q.enqueue(k)
            
    if q.front() == 0:
        print("Test 1 Başarılı")
    else:
        print("Test 1 Başarısız")
        
    while not q.isEmpty():
        lst2.append(q.dequeue())
            
    if lst2 != lst:
        print("Test 2 Başarısız")
    else:
        print("Test 2 Başarılı")
        
    for i in lst:
        q.enqueue(k)
            
    lst = []
        
    while not q.isEmpty():
        lst2.append(q.dequeue())
            
    if lst2 !=lst:
        print("Test 3 Başarısız")
    else:
        print("Test 3 Başarılı")
        
    try:
        q.dequeue()
        print("Test 4 Başarısız")
    except RuntimeError:  
        print("Test 4 Başarılı")
    except:
        print("Test 4 Başarısız")
            
    try:
        q.front()
        print("Test 5 Başarısız")
            
    except RuntimeError:
        print("Test 5 Başarılı")
    except:
        print("Test 5 Başarısız")
            
if __name__=="__main__":
    main()
                    
# Bu Python kodu, bir kuyruk veri yapısını temsil eden bir Queue sınıfı tanımlar. 
# Kuyruk, öğelerin sonuna eklenip önünden çıkarıldığı bir veri yapısıdır. 
# Bu sınıf, kuyruğun temel işlevlerini gerçekleştirmek için metodlar içerir: enqueue (kuyruğa öğe ekler), 
# dequeue (kuyruktan öğe çıkarır), front (kuyruğun önündeki öğeyi döndürür), ve isEmpty (kuyruğun boş olup olmadığını kontrol eder).
# Kod ayrıca, Queue sınıfının doğru çalışıp çalışmadığını test etmek için bir main fonksiyonu içerir. 
# Bu fonksiyon, bir dizi testi çalıştırır ve her biri için başarı veya başarısızlık durumunu yazdırır.
