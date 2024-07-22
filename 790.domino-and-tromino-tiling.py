#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#


# @lc code=start
from functools import lru_cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            """
            i is the higher line of the board
            j is the higher line of the board
            """
            if i > n or j > n:
                return 0
            if i == n and j == n:
                return 1

            # Vertical domino -> i+1 and j+1
            # Horizontal domino -> i+2 or j+2
            # 2 Horizontal dominos -> i+2 and j+2
            # Tromino -> i+2 and j+1
            # Inverse Tromino -> i+1 and j+2
            if i == j:
                return (
                    dp(i + 1, j + 1)
                    + dp(i + 2, j + 2)
                    + dp(i + 2, j + 1)
                    + dp(i + 1, j + 2)
                ) % MOD
            elif i < j:
                return dp(i + 2, j) + dp(i + 2, j + 1) % MOD
            else:
                return dp(i, j + 2) + dp(i + 1, j + 2) % MOD

        return dp(0, 0)


# @lc code=end
