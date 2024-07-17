#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
from typing import List


# @lc code=start
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), reverse=True, key=lambda x: x[1])

        nums1_heap: List[int] = []
        sum_nums1 = 0
        max_score = 0
        for num1, min_nums2 in nums:
            heapq.heappush(nums1_heap, num1)
            sum_nums1 += num1
            if len(nums1_heap) > k:
                min_num1 = heapq.heappop(nums1_heap)
                sum_nums1 -= min_num1
            if len(nums1_heap) == k:
                max_score = max(max_score, sum_nums1 * min_nums2)

        return max_score


# @lc code=end
