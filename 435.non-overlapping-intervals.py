#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        nb_intervals = 0
        biggest_end = -5 * 10**4 - 1
        for interval in intervals:
            if interval[0] < biggest_end:
                nb_intervals += 1
            else:
                biggest_end = interval[1]
        return nb_intervals


# @lc code=end
