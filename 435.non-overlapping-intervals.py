#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List, Set


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        overlap_intervals: Set[int] = set()
        cur_int = 0
        while cur_int < n:
            # print(f"cur={cur_int}")
            overlap_int = cur_int + 1
            # Next overlaps with cur
            while (
                overlap_int < n
                and intervals[cur_int][1] > intervals[overlap_int][0]
            ):
                # print(f"overlap={overlap_int}")
                if intervals[overlap_int][1] < intervals[cur_int][1]:
                    cur_int = overlap_int
                    # print(f"new cur={cur_int}")
                overlap_intervals.add(overlap_int)
                overlap_int += 1

            cur_int += 1
            while cur_int in overlap_intervals:
                cur_int += 1
        return len(overlap_intervals)


# @lc code=end
