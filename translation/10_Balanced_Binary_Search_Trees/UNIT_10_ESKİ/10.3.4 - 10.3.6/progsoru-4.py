import random

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Düğümün yüksekliği, başlangıçta 1 olarak ayarlanır.

class AVLTree:
    def __init__(self):
        self.root = None  # Ağacın kök düğümü, başlangıçta boştur.

    def insert(self, key):
        """
        AVL ağacına bir düğüm ekler.
        """
        if not self.root:
            self.root = AVLNode(key)
            print(f"{key} ağacın kökü olarak eklendi.")
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        AVL ağacına düğüm eklerken kullanılan yardımcı fonksiyon.
        """
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
            print(f"{key} düğümü, {node.key} düğümünün soluna eklendi.")
            if self._get_balance(node) > 1:
                if key < node.left.key:
                    return self._rotate_right(node)
                else:
                    node.left = self._rotate_left(node.left)
                    return self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key)
            print(f"{key} düğümü, {node.key} düğümünün sağına eklendi.")
            if self._get_balance(node) < -1:
                if key > node.right.key:
                    return self._rotate_left(node)
                else:
                    node.right = self._rotate_right(node.right)
                    return self._rotate_left(node)
        
        # Yükseklikleri güncelle
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        return node

    def _get_height(self, node):
        """
        Bir düğümün yüksekliğini döndürür.
        """
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """
        Bir düğümün dengesini hesaplar.
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z):
        """
        Sağa döndürme işlemi.
        """
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y

    def _rotate_left(self, z):
        """
        Sola döndürme işlemi.
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def inorder_traversal(self):
        """
        AVL ağacını iç sıralama gezisi ile dolaşır.
        """
        if not self.root:
            return []
        result = []
        stack = []
        current = self.root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.key)
                current = current.right
            else:
                break
        return result

def test_avl_tree():
    """
    AVL ağacını test etmek için bir test fonksiyonu.
    """
    avl_tree = AVLTree()
    data = random.sample(range(1000), 10)  # Rastgele veri oluştur
    print("Eklenecek Veriler:", data)
    for key in data:
        avl_tree.insert(key)
    sorted_data = sorted(data)
    print("Beklenen Sıralama:", sorted_data)
    print("AVL Ağacı Sıralama:", avl_tree.inorder_traversal())
    if avl_tree.inorder_traversal() == sorted_data:
        print("Test Başarılı: AVL Ağacı Sıralaması Doğru!")
        print("\n Himmet Can Umutlu")
    else:
        print("Test Başarısız: AVL Ağacı Sıralaması Hatalı!")
        print("\n Himmet Can Umutlu")

if __name__ == "__main__":
    test_avl_tree()
