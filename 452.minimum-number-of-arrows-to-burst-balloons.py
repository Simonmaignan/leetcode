#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
from typing import List


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        nb_arrows = 0
        previous_arrow = points[0][0] - 1
        for balloon_start, balloon_end in points:
            if previous_arrow < balloon_start:
                previous_arrow = balloon_end
                nb_arrows += 1

        return nb_arrows


# @lc code=end
