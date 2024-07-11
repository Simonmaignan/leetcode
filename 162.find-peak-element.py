#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[1] < nums[0]:
            return 0
        if nums[-2] < nums[-1]:
            return n - 1
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left


# @lc code=end
