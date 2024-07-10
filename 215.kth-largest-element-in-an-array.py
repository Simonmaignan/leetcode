#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
import heapq


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            k_largest = -heapq.heappop(heap)

        return k_largest


# @lc code=end
