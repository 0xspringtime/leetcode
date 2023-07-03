#trie
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use a dictionary as the main data structure
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for char in word:
            # If char is not in the current dictionary, add it
            if char not in node:
                node[char] = {}
            # Move to the next level
            node = node[char]
        # After inserting all the characters of the word, insert the end marker
        node['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for char in word:
            # If char is not in the current dictionary, return False
            if char not in node:
                return False
            # Move to the next level
            node = node[char]
        # If we've inserted all the characters of the word, return whether the end marker is there
        return '#' in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for char in prefix:
            # If char is not in the current dictionary, return False
            if char not in node:
                return False
            # Move to the next level
            node = node[char]
        # If we've inserted all the characters of the prefix, we can be sure that there's a word that starts with this prefix
        return True
#time O(n)
#space O(n)
