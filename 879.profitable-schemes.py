#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
from typing import List


# @lc code=start
class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        n_crimes = len(group)
        sum_profit = sum(profit)
        dp: List[List[int]] = [
            [[-1] * (n + 1) for _ in range(sum_profit + 1)] for _ in range(n_crimes + 1)
        ]

        def dfs(start_i: int, cur_profit: int, nb_members: int) -> int:
            if nb_members > n:
                return 0
            if dp[start_i][cur_profit][nb_members] >= 0:
                return dp[start_i][cur_profit][nb_members]

            nb_profitable_crimes = 0
            if cur_profit >= minProfit:
                nb_profitable_crimes += 1
            for i in range(start_i, n_crimes):
                nb_profitable_crimes += dfs(
                    i + 1, cur_profit + profit[i], nb_members + group[i]
                )

            dp[start_i][cur_profit][nb_members] = nb_profitable_crimes
            return nb_profitable_crimes

        return dfs(0, 0, 0) % (10**9 + 7)


# @lc code=end
