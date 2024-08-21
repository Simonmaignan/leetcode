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
        if n_n > h_n:
            return -1
        for h_i in range(h_n):
            h_j = h_i
            for char in needle:
                if char != haystack[h_j]:
                    break
                h_j += 1
                if h_j >= h_n:
                    break

            if h_j == (h_i + n_n):
                return h_i

        return -1


# @lc code=end
