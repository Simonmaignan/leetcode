#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
from typing import List


# @lc code=start
import numpy as np


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        np_grid = np.array(grid)

        nb_pairs = 0
        for row in np_grid:
            for col in np_grid.T:
                if np.array_equal(row, col):
                    nb_pairs += 1

        return nb_pairs


# @lc code=end
