#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        i = m + n - 1
        while i1 < i:
            # print(f"i={i}; i1={i1}; i2={i2}")
            if i1 < 0 or i2 >= 0 and nums2[i2] >= nums1[i1]:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
            # print(nums1)
            i -= 1


# @lc code=end
