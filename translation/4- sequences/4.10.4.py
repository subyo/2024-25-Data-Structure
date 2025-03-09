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

    def __init__(self, contents=None):  # contents'i None olarak değiştirdim
        """
        Bağlı Liste oluşturucu metodu.
        """
        # Listenin başını ve sonunu tutan dummy düğüm oluşturulur.
        self.first = self.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        if contents is not None:  # contents'i kontrol ettim
            for e in contents:
                self.append(e)

    def append(self, item):
        """
        Listenin sonuna bir öğe ekler.
        """
        new_node = self.__Node(item)
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
        while current is not None:
            string += str(current.getItem())
            if current.getNext() is not None:
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

    def __add__(self, other):
        """
        İki LinkedList nesnesini birleştirir.
        """
        if type(self) != type(other):
            raise TypeError(
                "Concatenate undefined for " + str(type(self)) + " + " + str(type(other))
            )

        result = LinkedList()

        cursor = self.first.getNext()

        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result


# Örnek Kullanım
if __name__ == "__main__":
    list1 = LinkedList([1, 2, 3])
    list2 = LinkedList([4, 5, 6])

    combined_list = list1 + list2
    print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

    try:
        combined_list = list1 + [7, 8, 9]  # TypeError
    except TypeError as e:
        print(e)

    print(list1[1])  # Output: 2
    list1[1] = 25
    print(list1)  # Output: [1, 25, 3]

    try:
        print(list1[5])
    except IndexError as e:
        print(e)  # Output: LinkedList index out of range