#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        r = len(nums) - 1
        while r >= 0 and nums[r] == val:
            r -= 1
        while k <= r:
            if nums[k] == val:
                nums[k], nums[r] = nums[r], nums[k]
                while r >= 0 and nums[r] == val:
                    r -= 1
            k += 1
        return k


# @lc code=end
