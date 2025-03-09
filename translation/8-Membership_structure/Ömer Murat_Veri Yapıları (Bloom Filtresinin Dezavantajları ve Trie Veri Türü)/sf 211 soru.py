class TrieNode:  
    def __init__(self, item=None):  
        self.item = item  
        self.children = {}  # Alt düğümleri tutmak için bir sözlük  
        self.is_end_of_word = False  # Kelime bitişi kontrolü  

class Trie:  
    def __init__(self):  
        self.root = TrieNode()  # Trie'nin kök düğümü  

    def _insert(self, node, item):  
        # Anahtarın her bir karakteri için düğüm oluştur  
        for char in item:  
            if char not in node.children:  
                node.children[char] = TrieNode(char)  
            node = node.children[char]  
        node.is_end_of_word = True  # Anahtarın sonuna geldiğimizi belirt  

    def insert(self, item):  
        self._insert(self.root, item)  

    def _contains(self, node, item):  
        for char in item:  
            if char not in node.children:  
                return False  # Düğüm yoksa anahtar yok  
            node = node.children[char]  
        return node.is_end_of_word  # Kök düğümden anahtarın sonunu kontrol et  

    def contains(self, item):  
        return self._contains(self.root, item)  

# Kullanım örneği  
trie = Trie()  
trie.insert("cat")  
trie.insert("cater")  
trie.insert("car")  

print(trie.contains("cat"))    # True  
print(trie.contains("cater"))  # True  
print(trie.contains("car"))    # True  
print(trie.contains("cats"))   # False  
print(trie.contains("dog"))    # False