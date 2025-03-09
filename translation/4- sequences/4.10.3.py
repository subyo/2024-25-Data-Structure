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

    def __getitem__(self, index):
        """
        Belirtilen indeksteki öğeyi döndürür.
        """
        if 0 <= index < self.numItems:  # İndeks sınırları kontrolü
            cursor = self.first.getNext()
            for _ in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        """
        Belirtilen indeksteki öğeyi belirtilen değerle değiştirir.
        """
        if 0 <= index < self.numItems:  # İndeks sınırları kontrolü
            cursor = self.first.getNext()
            for _ in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")


# Örnek Kullanım
if __name__ == '__main__':
    my_list = LinkedList([10, 20, 30])
    print(my_list[1])

    my_list[1] = 25
    print(my_list)

    try:
        print(my_list[5])
    except IndexError as e:
        print(e)