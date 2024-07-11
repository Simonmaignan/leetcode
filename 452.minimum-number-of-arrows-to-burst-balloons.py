#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
from typing import List


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        nb_arrows = 0
        start_overlap = 0
        end_overlaps = 0
        while start_overlap < n:
            while (
                end_overlaps < n
                and points[end_overlaps][0] <= points[start_overlap][1]
            ):
                end_overlaps += 1
            nb_arrows += 1
            start_overlap = end_overlaps
        return nb_arrows


# @lc code=end
