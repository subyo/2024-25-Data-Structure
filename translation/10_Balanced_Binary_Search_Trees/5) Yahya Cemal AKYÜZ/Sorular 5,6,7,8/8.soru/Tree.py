class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:  # x is root
            self.root = y

        elif x == x.parent.left:  # x is left child
            x.parent.left = y

        else:  # x is right child
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:  # x is root
            self.root = y

        elif x == x.parent.right:  # x is right child
            x.parent.right = y

        else:  # x is left child
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent != None:  # node is not root
            if n.parent == self.root:  # node is child of root, one rotation
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)

            else:
                p = n.parent
                g = p.parent  # grandparent

                if n.parent.left == n and p.parent.left == p:  # both are left children
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif n.parent.right == n and p.parent.right == p:  # both are right children
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def lookup(self, n, x):
        if x == n.data:
            self.splay(n)
            return n

        elif x < n.data:
            return self.lookup(n.left, x)
        elif x > n.data:
            return self.lookup(n.right, x)
        else:
            return None

    def delete(self, n):
        self.splay(n)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root != None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root != None:
            right_subtree.root.parent = None

        if left_subtree.root != None:
            m = left_subtree.maximum(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

class AvlNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return AvlNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def lookup(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.lookup(root.right, value)
        return self.lookup(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def lookup_value(self, value):
        return self.lookup(self.root, value)



