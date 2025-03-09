class Trie:
    def __insert(node,item):
        # Bu özyinelemeli insert fonksiyonudur

    def __contains(node,item):
         # Bu özyinelemeli üyelik testidir.

    class TrieNode:
        def __init__(self,item,next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows

    def __init__(self):
        self.start = None

    def init(self, item):
        self.start = None

    def insert(self, item):
        self.start = Trie.__insert(self.start, item)

    def __contains__(self,item):
        return Trie_contains(self ,Start ,item)