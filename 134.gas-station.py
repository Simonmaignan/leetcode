#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # pref_diff = [0]
        # ans = (-1, -1)
        # for i in range(n):
        #     pref_diff[i + 1] = pref_diff[i] + gas[i] - cost[i]
        #     if pref_diff[i + 1] > ans[1]:
        #         ans = (i, pref_diff[i + 1])
        # return ans[0]
        diff = [gas[i] - cost[i] for i in range(n)]
        for i in range(n):
            # print(f"i={i}")
            tank = diff[i]
            j = (i + 1) % n
            # print(f"j={j}")
            # print(f"tank={tank}")
            while j != i and tank >= 0:
                # print(f"j={j}")
                # print(f"tank={tank}")
                tank += diff[j]
                j = (j + 1) % n
            if tank >= 0:
                return i
        return -1


# @lc code=end
