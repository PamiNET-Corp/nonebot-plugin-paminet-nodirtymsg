from typing import List

class TrieNode:
    __slots__ = ("children", "is_end")
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class BadWordsFilter:
    def __init__(self):
        self.root = TrieNode()
    
    def build(self, words: List[str]):
        """构建Trie树"""
        for word in words:
            if not word:
                continue
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
    
    def search(self, text: str) -> bool:
        """搜索违禁词"""
        text = text.lower()
        n = len(text)
        for i in range(n):
            node = self.root
            for j in range(i, n):
                char = text[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end:
                    return True
        return False