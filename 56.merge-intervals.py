#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda list: list[0])
        merged_intervals: List[List[int]] = []
        n = len(intervals)
        merged_start = intervals[0][0]
        merged_end = intervals[0][1]
        i = 1
        while i < n:
            start_i, end_i = intervals[i][0], intervals[i][1]
            if start_i > merged_end:
                merged_intervals.append([merged_start, merged_end])
                merged_start = start_i
                merged_end = end_i
                i += 1
                continue
            merged_end = max(merged_end, end_i)
            i += 1
        merged_intervals.append([merged_start, merged_end])
        return merged_intervals


# @lc code=end
