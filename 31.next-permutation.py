#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from typing import List


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Find first number from the end lower than its follower
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # print(f"i={i}")
        if i >= 0:
            # Find smallest number higher than nums[i] between i+1 and n
            j = i + 1
            smallest = nums[j]
            for k in range(i + 2, n):
                # print(f"k={k}; num={nums[k]}; j={j}; smallest={smallest}")
                if nums[i] < nums[k] <= smallest:
                    j = k
                    smallest = nums[k]
            # print(f"j={j}")
            # Swap i and j
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums)
        # Reverse nums[i+1:]
        i += 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# @lc code=end
