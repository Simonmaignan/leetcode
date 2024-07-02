#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from typing import List, Tuple

# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h: List[Tuple[int, List[int]]] = []

        for point in points:
            dist_to_origin = point[0] ** 2 + point[1] ** 2
            heapq.heappush(h, (dist_to_origin, point))

        return [heapq.heappop(h)[1] for _ in range(k)]


# @lc code=end
