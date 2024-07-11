#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
from typing import List


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        reversed_words: List[str] = []
        while right >= 0:
            while right >= 0 and s[right] == " ":
                right -= 1
            if right < 0:
                break
            left = right - 1
            while left >= 0 and s[left] != " ":
                left -= 1
            reversed_words.append(s[left + 1 : right + 1])
            right = left - 1
        return " ".join(reversed_words)


# @lc code=end
