#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        spiral_order: List[int] = []
        navigation: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        min_i, max_i = 0, m
        min_j, max_j = 0, n
        i, j = min_i, min_j

        while min_i < max_i or min_j < max_j:
            




# @lc code=end
