#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: List[List[int]] = [
            [0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)
        ]

        for i1, c1 in enumerate(text1):
            for i2, c2 in enumerate(text2):
                if c1 == c2:
                    dp[i1 + 1][i2 + 1] = dp[i1][i2] + 1
                else:
                    dp[i1 + 1][i2 + 1] = max(dp[i1][i2 + 1], dp[i1 + 1][i2])

        return dp[-1][-1]


# @lc code=end
