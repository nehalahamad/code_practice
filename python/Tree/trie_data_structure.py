"""Trie data structure also known as PrefixTree, it is derived from Retrieval (reTRIEval)
Leetcode -> 
    208. Implement Trie (Prefix Tree) (https://leetcode.com/problems/implement-trie-prefix-tree/description/)
        Youtube -> https://youtu.be/oobqoCJlHA0
    1268. Search Suggestions System (https://leetcode.com/problems/search-suggestions-system/description/)
"""
from typing import List


# ------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.end_of_word: bool = False
# ------------------------------------------------
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word:str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word

    def startsWith(self, word:str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for prod in products:
            t.insert(prod)
        
        cur = t.root
        for c in searchWord:
            if c in cur.children:
                print(cur.children.keys())
            cur = cur.children[c]


s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
s.suggestedProducts(products, searchWord)