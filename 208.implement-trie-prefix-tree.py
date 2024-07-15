#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from typing import Dict, Optional


# @lc code=start
class Trie:

    def __init__(self):
        self.children: Dict[str, Trie] = {}
        self.end_of_word = 0

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.end_of_word += 1

    def _search_prefix(self, prefix: str) -> Optional["Trie"]:
        node = self
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node.end_of_word != 0 if node is not None else False

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return True if node is not None else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
