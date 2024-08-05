#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        return [1] + digits


# @lc code=end
