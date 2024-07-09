#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#
from typing import List, Set


# @lc code=start
class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        ans: List[List[int]] = []
        nums1_set: Set[int] = set(nums1)
        nums2_set: Set[int] = set(nums2)

        ans.append(list(nums1_set - nums2_set))
        ans.append(list(nums2_set - nums1_set))

        return ans


# @lc code=end
