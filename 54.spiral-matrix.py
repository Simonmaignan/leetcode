#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List, Tuple


# @lc code=start
# from pprint import pprint


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        spiral_order: List[int] = []
        directions: List[Tuple[int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        MIN_NUM = -101
        i = j = k = 0
        while len(spiral_order) < (m * n):
            # print(spiral_order)
            while 0 <= i < m and 0 <= j < n and matrix[i][j] > MIN_NUM:
                # print(f"i={i}; j={j}; k={k}")
                spiral_order.append(matrix[i][j])
                matrix[i][j] = MIN_NUM
                i += directions[k][0]
                j += directions[k][1]
                # print(spiral_order)
                # pprint(visited)
            # Come back one step
            i -= directions[k][0]
            j -= directions[k][1]
            # Change directions
            k = (k + 1) % len(directions)
            # Next step
            i += directions[k][0]
            j += directions[k][1]

        return spiral_order


# @lc code=end
