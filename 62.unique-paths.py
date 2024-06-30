#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
from typing import List


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[List[int]] = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


# @lc code=end
