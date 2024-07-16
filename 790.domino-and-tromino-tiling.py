#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
from typing import List


# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Upper row
        for i in range(1, n + 1):
            # Lower row
            for j in range(1, n + 1):
                # Placing a domino vertically
                dp[i][j] += dp[i - 1][j - 1]
                if i >= 2:
                    # Placing a tromino tile
                    dp[i][j] += dp[i - 2][j - 1]
                if j >= 2:
                    # Placing a tromino tile
                    dp[i][j] += dp[i - 1][j - 2]
                if i >= 2 and j >= 2:
                    # Placing 2 dominos horizontally
                    dp[i][j] += dp[i - 2][j - 2]

        return dp[-1][-1] % (10**9 + 7)


# @lc code=end
