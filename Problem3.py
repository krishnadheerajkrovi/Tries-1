'''
1. Insert all words of dictionary into the trie.
2. We go word by word and check character by character in each word if it starts with any dictionary's word using Trie
3. If we reach end of dictionary's word then we append the characters captured till now( same as dict word) in a temp list. 
4. Else we keep the original word

TC: O(nl + mk) where n is number of words in dictionary, l is length of them, m is number of words in sentence and k is their avg length
'''

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.children[ord(c) - ord('a')]:
                cur.children[ord(c) - ord('a')] = self.TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.isEnd = True
  
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if not dictionary or len(dictionary) == 0:
            return sentence
        
        self.root = self.TrieNode()
        for word in dictionary:
            self.insert(word)

        strArr = sentence.split()
        res = []
        for word in strArr:
            cur = self.root
            replacement = []
            for i in range(len(word)):
                c = word[i]
                if not cur.children[ord(c) - ord('a')] or cur.isEnd:
                    break
                replacement.append(c)
                cur = cur.children[ord(c)- ord('a')]
            if cur.isEnd:
                res.append(''.join(replacement))
            else:
                res.append(word)
    
        return ' '.join(res)
