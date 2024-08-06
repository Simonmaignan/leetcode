#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        i = 0
        while True:
            next_char = ""
            for string in strs:
                if i >= len(string):
                    next_char = ""
                    break
                if not next_char:
                    next_char = string[i]
                elif string[i] != next_char:
                    next_char = ""
                    break

            if not next_char:
                return longest_common_prefix
            longest_common_prefix += next_char
            i += 1


# @lc code=end
