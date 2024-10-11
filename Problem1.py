'''
1. Have a TrieNode class defined that has 26 children (one for each letter a-z) and one flag to know that node is end of a word
2. Start with a root node and keep inserting letter by letter. Each letter is a TrieNode again with children
3. Search follows the same but if at any place we couldn't find a child or if the end flag is False for that word it is not found
4. Prefix is similar but we need not check for end flag but only the path

TC: O(n)
SC: O(m) where m can be length of longest word
'''

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.children[ord(c) - ord('a')]:
                cur.children[ord(c) - ord('a')] = self.TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return True 