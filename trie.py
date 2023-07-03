class TrieNode:
    def __init__(self):
        """
        Initialize TrieNode here.
        Each node will have a dictionary 'children' and a boolean 'is_word' to mark end of a word.
        """
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize Trie (Prefix Tree) here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into Trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the Trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the Trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

#main advantage of Trie is its ability to search, insert, and delete strings in O(L) time complexity, where L is the length of the string

#Trie is well-suited for building a dictionary of words and efficiently finding all words with a given prefix, checking if a word exists in a dictionary, or deleting a word from it.
