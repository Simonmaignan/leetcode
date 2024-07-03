#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import Dict, List


# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children: Dict[str, "Trie"] = {}
        self.end_of_word = False

    def __str__(self) -> str:
        display_msg = ""
        for char, trie_node in self.children.items():
            display_msg += char
            display_msg += f" {str(trie_node)}"
        if self.end_of_word:
            display_msg += " eow "
        return display_msg

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.end_of_word = True

    def find_word(self, word: str, start_i: int) -> List[int]:
        # print(f"find_word {word} from {start_i}")
        end_indexes: List[int] = []
        node = self
        # print(f"root node with {node.children.keys()}; {node.end_of_word}")
        n = len(word)
        for i in range(start_i, n):
            char = word[i]
            # print(f"word[{i}]={char}")
            if char not in node.children:
                return end_indexes
            node = node.children[char]
            if node.end_of_word:
                end_indexes.append(i + 1)
            #     print(f"end_i={end_indexes}")
            # print(f"node with {node.children.keys()}; {node.end_of_word}")

        return end_indexes


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        # print(trie)

        n = len(s)
        memo: List[bool] = [False] * n

        def dfs(start_i: int) -> bool:
            # print(f"start_i={start_i}")
            if start_i == n:
                return True

            if memo[start_i]:
                return False

            for end_i in trie.find_word(s, start_i):
                # print(f"end_i={end_i}")
                if dfs(end_i):
                    return True

            memo[start_i] = True
            return False

        return dfs(0)


# @lc code=end
