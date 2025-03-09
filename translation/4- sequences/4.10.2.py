class LinkedList:
    """
    Bağlı Liste veri yapısı.
    """

    class __Node:
        """
        Bağlı Listenin iç yapısı olan Düğüm sınıfı.
        """
        def __init__(self, item, next=None):
            """
            Düğüm oluşturucu metodu.
            """
            self.item = item
            self.next = next

        def getItem(self):
            """
            Düğümün değerini döndürür.
            """
            return self.item

        def getNext(self):
            """
            Sonraki düğümü döndürür.
            """
            return self.next

        def setItem(self, item):
            """
            Düğümün değerini ayarlar.
            """
            self.item = item

        def setNext(self, next):
            """
            Sonraki düğümü ayarlar.
            """
            self.next = next

    def __init__(self, contents=[]):
        """
        Bağlı Liste oluşturucu metodu.
        """
        # Listenin başını ve sonunu tutan dummy düğüm oluşturulur.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def append(self, item):
        """
        Listenin sonuna bir öğe ekler.
        """
        new_node = LinkedList.__Node(item)
        self.last.setNext(new_node)
        self.last = new_node
        self.numItems += 1

    def __len__(self):
        """
        Listedeki öğe sayısını döndürür.
        """
        return self.numItems

    def __str__(self):
        """
        Listeyi okunabilir bir string olarak döndürür.
        """
        string = "["
        current = self.first.getNext()
        while current:
            string += str(current.getItem())
            if current.getNext():
                string += ", "
            current = current.getNext()
        string += "]"
        return string

# Örnek Kullanım
if __name__ == '__main__':
    my_list = LinkedList([1, 2, 3])
    print(my_list)  # Output: [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    print(len(my_list))  # Output: 4