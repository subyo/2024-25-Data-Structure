class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PlusNode(Node):
    def __init__(self):
        super().__init__('+')

class TimesNode(Node):
    def __init__(self):
        super().__init__('*')

# 5 * 4 + 3 * 2 ifadesi için ağaç yapısını kurma

# Adım 1: Çarpma işlemleri
times1 = TimesNode()  # 5 * 4 işlemi
times1.left = Node(5)
times1.right = Node(4)

times2 = TimesNode()  # 3 * 2 işlemi
times2.left = Node(3)
times2.right = Node(2)

# Adım 2: Toplama işlemi
plus = PlusNode()  # 5 * 4 + 3 * 2 işlemi
plus.left = times1
plus.right = times2

# Ağaç yapısını yazdırma fonksiyonu
def print_tree(node, level=0):
    if node != None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)

# Ağaç yapısını yazdır
print_tree(plus)