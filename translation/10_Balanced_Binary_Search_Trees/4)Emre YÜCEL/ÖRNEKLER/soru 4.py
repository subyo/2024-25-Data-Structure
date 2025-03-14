class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Başlangıçta düğüm yüksekliği 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Bir düğümün yüksekliğini al
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Bir düğümün denge faktörünü al
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Sağ rotasyon
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Rotasyonu gerçekleştir
        x.right = y
        y.left = T2

        # Yükseklikleri güncelle
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        # Yeni kökü döndür
        return x

    # Sol rotasyon
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Rotasyonu gerçekleştir
        y.left = x
        x.right = T2

        # Yükseklikleri güncelle
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        # Yeni kökü döndür
        return y

    # Iteratif olarak bir düğüm ekle
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        stack = []
        current = self.root
        while current:
            stack.append(current)
            if key < current.key:
                if not current.left:
                    current.left = Node(key)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(key)
                    break
                current = current.right

        # Eklenen düğümün her üst düğümünün yüksekliğini güncelle
        while stack:
            node = stack.pop()
            node.height = 1 + max(self.height(node.left), self.height(node.right))

            # Bu düğümün denge faktörünü al
            balance = self.get_balance(node)

            # Eğer düğüm dengesizse, rotasyon yap
            if balance > 1 and key < node.left.key:
                node = self.right_rotate(node)
            elif balance < -1 and key > node.right.key:
                node = self.left_rotate(node)
            elif balance > 1 and key > node.left.key:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
            elif balance < -1 and key < node.right.key:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)

            # Kök düğümünü güncelle
            if stack:
                parent = stack[-1]
                if parent.left == node or parent.right == node:
                    continue
            self.root = node

    # İleri (in-order) dolaşım yöntemi
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)

# Test Programı
import random

def test_avl_tree():
    tree = AVLTree()
    # 1 ile 100 arasında 20 rastgele sayı üret
    random_numbers = random.sample(range(1, 101), 20)
    
    print("Ekleme yapılan sayılar:", random_numbers)
    
    # Rastgele sayıları AVL ağacına ekle
    for num in random_numbers:
        tree.insert(num)
    
    print("\nAVL ağacının sıralı (in-order) dolaşımı:")
    tree.in_order_traversal(tree.root)

# Testi çalıştır
test_avl_tree()
