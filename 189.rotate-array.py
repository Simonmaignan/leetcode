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
        k %= n
        # Reverse nums
        for i in range(n // 2):
            nums[i], nums[-i - 1] = nums[-i - 1], nums[i]

        # Reverse k first elements
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

        # Reverse n-k last elements
        for i in range((n - k) // 2):
            nums[k + i], nums[-i - 1] = nums[-i - 1], nums[k + i]


# @lc code=end
