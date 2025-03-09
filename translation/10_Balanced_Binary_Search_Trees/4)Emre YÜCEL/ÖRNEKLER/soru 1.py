import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def pre_order(self, node):
        if not node:
            return []
        return [node.key] + self.pre_order(node.left) + self.pre_order(node.right)

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    test_data = random.sample(range(1, 100), 10)
    print("Rastgele eklenen veriler:", test_data)
    
    for num in test_data:
        root = avl.insert(root, num)
    
    print("AVL ağacının pre-order gezintisi:", avl.pre_order(root))
