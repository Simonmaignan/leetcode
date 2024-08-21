#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_n = len(haystack)
        n_n = len(needle)
        for h_i in range(h_n - n_n + 1):
            if haystack[h_i : h_i + n_n] == needle:
                return h_i

        return -1


# @lc code=end
