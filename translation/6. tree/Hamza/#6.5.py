#6.5


class BinarySearchTree:
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            if root is None:
                return BinarySearchTree.__Node(val)

            if val < root.val:
                root.left = __insert(root.left, val)
            else:
                root.right = __insert(root.right, val)

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()

def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()


# klavyeden 5 8 2 1 4 9 6 7 

