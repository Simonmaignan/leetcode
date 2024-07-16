#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
from typing import Dict, List


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
                node.children = dict(sorted(node.children.items()))
            node = node.children[char]
        node.end_of_word = True

    def get_suggestions(self, word: str) -> List[List[str]]:
        n = len(word)

        def dfs(
            node: Trie,
            start_i: int,
            cur_path: List[str],
            search_suggestions: bool,
            sub_suggestions: List[str],
            suggestions: List[List[str]],
        ) -> None:
            if not search_suggestions:
                if start_i == n:
                    return
                if word[start_i] in node.children:
                    # Search for suggestions at start_i
                    cur_path.append(word[start_i])
                    dfs(
                        node.children[word[start_i]],
                        start_i,
                        cur_path,
                        True,
                        sub_suggestions,
                        suggestions,
                    )
                    suggestions[start_i] = sub_suggestions[:]
                    sub_suggestions.clear()
                    # Go to next char in word
                    dfs(
                        node.children[word[start_i]],
                        start_i + 1,
                        cur_path,
                        False,
                        sub_suggestions,
                        suggestions,
                    )
            else:
                if len(sub_suggestions) == 3:
                    return
                if node.end_of_word:
                    sub_suggestions.append("".join(cur_path))
                for char, child in node.children.items():
                    cur_path.append(char)
                    dfs(
                        child,
                        start_i,
                        cur_path,
                        True,
                        sub_suggestions,
                        suggestions,
                    )
                    cur_path.pop()

        suggestions: List[List[int]] = [[] for _ in range(n)]
        dfs(self, 0, [], False, [], suggestions)
        return suggestions


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        return trie.get_suggestions(searchWord)


# @lc code=end
