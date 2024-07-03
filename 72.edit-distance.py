#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
from typing import List


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        dp: List[List[int]] = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i1 in range(n1 + 1):
            dp[i1][0] = i1

        for i2 in range(n2 + 1):
            dp[0][i2] = i2

        for i1, c1 in enumerate(word1):
            for i2, c2 in enumerate(word2):
                if c1 == c2:
                    dp[i1 + 1][i2 + 1] = dp[i1][i2]
                else:
                    dp[i1 + 1][i2 + 1] = (
                        min(dp[i1][i2 + 1], dp[i1 + 1][i2], dp[i1][i2]) + 1
                    )

        return dp[-1][-1]


# @lc code=end
