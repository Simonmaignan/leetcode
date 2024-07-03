#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        n1 = len(word1)
        n2 = len(word2)
        merged_str = ""
        while p1 < n1 or p2 < n2:
            if p1 < n1:
                merged_str += word1[p1]
                p1 += 1
            if p2 < n2:
                merged_str += word2[p2]
                p2 += 1
        return merged_str


# @lc code=end
