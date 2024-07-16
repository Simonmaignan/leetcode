#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
from typing import List, Tuple
from collections import Counter


# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)
        # print(row_counter)
        nb_pairs = 0
        for c in range(n):
            col_tuple: Tuple[int] = tuple(grid[r][c] for r in range(n))
            # print(col_tuple)
            nb_pairs += row_counter[col_tuple]
        return nb_pairs


# @lc code=end
