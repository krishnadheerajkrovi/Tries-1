'''
1. We use a Trie to identify the longest word built by adding chars to a word. First add all words to a trie 
2. For each word, keep a track from root of trie if at each child, end of word flag is True (meaning its a word)
3. If no break for that word. In case a longer word is found, update the result
4. Whereas in case same length word is encountered, update only if its lexicographically smaller

TC: O(n)
SC: O(n)
'''

class Trie:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isEnd = False

        def __init__(self):
            self.root = self.TrieNode()
            
        def insert(self, word: str) -> None:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = self.TrieNode()
                cur = cur.children[c]
            cur.isEnd = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = ''
        for word in words:
            if len(word) < len(res): continue

            cur = trie.root

            for c in word:
                cur = cur.children[c]
                if not cur.isEnd: break
            
            if cur.isEnd and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word
        return res