#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_intervals: List[List[int]] = []
        start_new, end_new = newInterval[0], newInterval[1]
        i = 0
        n = len(intervals)

        if n == 0:
            return [newInterval]

        while i < n and intervals[i][1] < start_new:
            new_intervals.append(intervals[i])
            i += 1

        start_merge = start_new
        end_merge = end_new
        while i < n and intervals[i][0] <= end_new:
            # print(intervals[i])
            start_merge = min(start_merge, intervals[i][0])
            # print(f"start_merge={start_merge}")
            end_merge = max(end_merge, intervals[i][1])
            # print(f"end_merge={end_merge}")
            i += 1
        new_intervals.append([start_merge, end_merge])

        while i < n:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals


# @lc code=end
