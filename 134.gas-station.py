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
        start = end = n - 1
        visited_station = 0
        tank = 0
        while visited_station < n:
            tank += gas[end] - cost[end]
            end = (end + 1) % n
            visited_station += 1
            # print(f"start={start}")
            # print(f"end={end}")
            # print(f"tank={tank}")
            while tank < 0 and visited_station < n:
                start = (start - 1) % n
                tank += gas[start] - cost[start]
                visited_station += 1
        return start if tank >= 0 else -1


# @lc code=end
