8#Önceki alıştırmada olduğu gibi bir trie oluşturun, ancak yanlış yazılan tüm kelimeler için önerilen değişiklikleri de yazdırın. Bu zor bir ödevdir. Önerilen değişiklikler orijinalinden bölümde önerilen yollardan birden fazlasıyla farklı olmamalıdır. 


import nltk 

nltk.download('words') 

from nltk.corpus import words 

  

class TrieNode: 

    def __init__(self): 

        self.children = {} 

        self.is_end_of_word = False 

        self.suggestions = [] 

  

class Trie: 

    def __init__(self): 

        self.root = TrieNode() 

  

    def insert(self, word): 

        node = self.root 

        for char in word: 

            if char not in node.children: 

                node.children[char] = TrieNode() 

            node = node.children[char] 

        node.is_end_of_word = True 

  

    def search(self, word): 

        node = self.root 

        for char in word: 

            if char not in node.children: 

                return False 

            node = node.children[char] 

        return node.is_end_of_word 

  

    def generate_suggestions(self, node, word): 

        if node.is_end_of_word: 

            print(f"Correct word: {word}") 

        for char, child_node in node.children.items(): 

            new_word = word + char 

            self.generate_suggestions(child_node, new_word) 

  

    def suggest_corrections(self, word): 

        node = self.root 

        for char in word: 

            if char not in node.children: 

                return 

            node = node.children[char] 

        self.generate_suggestions(node, word) 

  

# Create a Trie from the NLTK word list 

trie = Trie() 

for word in words.words(): 

    trie.insert(word) 

  

# Test the Trie with a misspelled word 

misspelled_word = "ue" 

if not trie.search(misspelled_word): 

    trie.suggest_corrections(misspelled_word) 

 