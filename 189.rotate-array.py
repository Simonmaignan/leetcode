#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_copy: List[int] = nums[:]
        for i in range(n):
            nums[i] = nums_copy[(n - k + i) % n]


# @lc code=end
