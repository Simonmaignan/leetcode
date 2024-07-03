#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)


# @lc code=end
