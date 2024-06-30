#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp: List[List[int]] = [[0] * n for _ in range(m)]

        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1

        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # print(dp)

        return dp[-1][-1]


# @lc code=end
