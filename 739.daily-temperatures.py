#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer: List[int] = [0] * n
        temp_stack: List[Tuple[int, int]] = []
        for i, temp in enumerate(temperatures):
            while temp_stack and temp_stack[-1][1] < temp:
                prev_i, _ = temp_stack.pop()
                answer[prev_i] = i - prev_i
            temp_stack.append((i, temp))
        return answer


# @lc code=end
