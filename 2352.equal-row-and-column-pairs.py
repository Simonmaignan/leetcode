#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
from typing import List, Dict
from collections import defaultdict


# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_dict: Dict[str, int] = defaultdict(int)
        for c in range(n):
            col_str = ""
            for r in range(n):
                col_str += f" {grid[r][c]}"
            col_dict[col_str] += 1

        nb_pairs = 0
        for r in range(n):
            row_str = ""
            for c in range(n):
                row_str += f" {grid[r][c]}"
            if row_str in col_dict:
                nb_pairs += col_dict[row_str]

        return nb_pairs


# @lc code=end
