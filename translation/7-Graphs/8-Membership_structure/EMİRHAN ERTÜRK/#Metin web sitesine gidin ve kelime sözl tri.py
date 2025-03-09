#Metin web sitesine gidin ve kelime sözlüğünü indirin. Bu sözcük listesi için bir trie veri türü oluşturun ve bağımsızlık bildirgesini yazım denetimi yapmak için kullanın, yanlış yazılan tüm sözcükleri ekrana yazdırın 


class TrieNode: 

    def __init__(self): 

        self.edges = [None] * 26 

        self.ends_here = False 

  

class Trie: 

    def __init__(self): 

        self.root = TrieNode() 

  

    def insert(self, word): 

        node = self.root 

        for char in word: 

            index = ord(char) - ord('a') 

            if node.edges[index] is None: 

                node.edges[index] = TrieNode() 

            node = node.edges[index] 

        node.ends_here = True 

  

    def search(self, word): 

        node = self.root 

        for char in word: 

            index = ord(char) - ord('a') 

            if node.edges[index] is None: 

                return False 

            node = node.edges[index] 

        return node is not None and node.ends_here 

  

    def delete_word(self, word): 

        def _delete_word(node, word, index): 

            if index == len(word): 

                if not node.ends_here: 

                    return "Word doesn't exist in the Trie" 

                node.ends_here = False 

                return "Deleted" 

  

            char = word[index] 

            index = ord(char) - ord('a') 

            if node.edges[index] is None: 

                return "Word doesn't exist in the Trie" 

  

            result = _delete_word(node.edges[index], word, index + 1) 

            if result == "Deleted": 

                node.edges[index] = None 

                if not node.ends_here: 

                    return "Deleted" 

  

            return result 

  

        _delete_word(self.root, word, 0) 

  

  

def load_words(filename): 

    with open(filename, 'r') as f: 

        words = [line.strip() for line in f.readlines()] 

    return words 

  

  

def check_spelling(trie, words): 

    for word in words: 

        if not trie.search(word): 

            print(f"{word} yanlış yazılmış.") 

  

  

if __name__ == "__main__": 

    # Indirme işlemini buraya ekleyin 

    word_list = load_words("indirilen_kelime_listesi.txt") 

  

    # Trie oluşturma işlemini buraya ekleyin 

    trie = Trie() 

    for word in word_list: 

        trie.insert(word) 

  

    # Yazım denetimi işlemini buraya ekleyin 

    with open("manifesto.txt", "r") as file: 

        text = file.read() 

        words = text.split() 

        check_spelling(trie, words) 