class Trie:
    class TrieNode:                                                                       
        def __init__(self, item, next=None, follows=None):
            self.item = item
            self.next = next
            self.follows = follows

    def __init__(self):
        self.start = None

    def insert(self, item):
        self.start = self.__insert(self.start, item)

    def __contains__(self, item):
        return self.__contains_recursive(self.start, item)

    def __insert(self, node, item):
        if node is None:
            return self.TrieNode(item)
        elif item < node.item:
            node.next = self.__insert(node.next, item)
        elif item > node.item:
            node.follows = self.__insert(node.follows, item)
        return node

    def __contains_recursive(self, node, item):
        if node is None:
            return False
        elif item == node.item:
            return True
        elif item < node.item:
            return self.__contains_recursive(node.next, item)
        else:
            return self.__contains_recursive(node.follows, item)

# Örnek kullanım:
trie = Trie()
trie.insert('apple')
trie.insert('banana')
print('apple' in trie)  # True
print('cherry' in trie)  # False
