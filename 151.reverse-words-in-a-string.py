#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        return " ".join(reversed(split_s))


# @lc code=end
