class Node:
    """
    Bağlı listede bir düğümü temsil eden sınıf.
    """
    def __init__(self, item, next=None):
        """
        Düğümün oluşturucu metodu.

        Args:
            item: Düğümün saklayacağı veri.
            next: Sonraki düğüme işaretçi (varsayılan olarak None).
        """
        self.item = item  # Düğümün verisini saklar
        self.next = next  # Sonraki düğüme işaretçi

    def getItem(self):
        """
        Düğümün verisini döndürür.

        Returns:
            Düğümün verisi.
        """
        return self.item

    def getNext(self):
        """
        Sonraki düğümü döndürür.

        Returns:
            Sonraki düğüm veya None (eğer son düğüm ise).
        """
        return self.next

    def setItem(self, item):
        """
        Düğümün verisini günceller.

        Args:
            item: Yeni veri.
        """
        self.item = item

    def setNext(self, next):
        """
        Sonraki düğümü ayarlar.

        Args:
            next: Sonraki düğüm.
        """
        self.next = next

# Örnek Kullanım:
if __name__ == '__main__':
    # Birkaç düğüm oluşturalım
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    # Düğümleri birbirine bağlayalım
    node1.setNext(node2)  # node1 -> node2
    node2.setNext(node3)  # node2 -> node3

    # Bağlı listeyi gezelim ve değerleri yazdıralım
    current_node = node1
    while current_node:
        print(current_node.getItem())
        current_node = current_node.getNext()