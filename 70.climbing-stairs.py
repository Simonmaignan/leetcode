#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from typing import List


# @lc code=start
class Solution:
    def climbStairs_(self, n: int) -> int:
        dp: List[int] = [-1] * n

        def dfs(remaining_steps) -> int:
            # print(f"remaining_steps={remaining_steps}")
            if remaining_steps == 0:
                return 1
            if dp[remaining_steps - 1] >= 0:
                return dp[remaining_steps - 1]

            nb_ways = 0
            for step in [1, 2]:
                # print(f"remaining_steps={remaining_steps}; step={step}")
                if step > remaining_steps:
                    continue
                nb_ways += dfs(remaining_steps - step)
            dp[remaining_steps - 1] = nb_ways
            # print(f"dp={dp}")
            return nb_ways

        return dfs(n)

    def climbStairs(self, n: int) -> int:
        dp: List[int] = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]


# @lc code=end
