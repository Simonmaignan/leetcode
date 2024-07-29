#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        k = r = 1
        while r < n:
            while r < n and nums[k - 1] == nums[r]:
                r += 1
            if r < n:
                if r != k:
                    nums[k] = nums[r]
                r += 1
                k += 1
        return k


# @lc code=end
