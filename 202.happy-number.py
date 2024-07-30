#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
from typing import Dict


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        n_map: Dict[int, int] = {}
        while True:
            if n == 1:
                return True
            if n in n_map:
                return False
            old_n = n
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit * digit
            n_map[old_n] = total_sum
            n = total_sum


# @lc code=end
