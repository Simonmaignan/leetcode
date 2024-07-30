#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        right = n - 1
        while s[right] == " ":
            right -= 1
        left = right
        while left >= 0 and s[left] != " ":
            left -= 1
        return right - left


# @lc code=end
