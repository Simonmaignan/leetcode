#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num = mid_num = inf
        for num in nums:
            print(f"num={num}; min_num={min_num}; mid_num={mid_num}")
            if num < min_num:
                min_num = num
            elif min_num < num < mid_num:
                mid_num = num
            elif num > mid_num:
                return True

        return False


# @lc code=end
