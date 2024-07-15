#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
from typing import Dict, List, Optional


# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children: Dict[str, Trie] = {}
        self.end_of_word = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
                node.children = dict(sorted(node.children))
            node = node.children[char]
        node.end_of_word = True

    def _search_prefix(self, prefix: str) -> Optional["Trie"]:
        node = self
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_suggestions(self, word: str) -> List[List[str]]:
        n = len(word)

        def dfs(
            node: Trie,
            start_i: int,
            cur_path: List[str],
            sub_suggestions: List[str],
            suggestions: List[List[int]],
        ) -> None:
            if start_i

        suggestions: List[List[int]] = []


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)


# @lc code=end
