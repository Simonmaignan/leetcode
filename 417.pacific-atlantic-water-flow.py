#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
from collections import deque

# from pprint import pprint
from typing import List, Tuple


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def get_neighbors(coord: Tuple[int]) -> List[Tuple[int]]:
            # print(f"get neighbors from {coord}")
            directions: List[Tuple[int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            neighbors: List[Tuple[int]] = []
            for direction in directions:
                neighbor_coord: Tuple[int] = (
                    coord[0] + direction[0],
                    coord[1] + direction[1],
                )
                if 0 <= neighbor_coord[0] < m and 0 <= neighbor_coord[1] < n:
                    neighbors.append(neighbor_coord)
            return neighbors

        falls_into: List[List[str]] = [[""] * n for _ in range(m)]
        pacific_cost: List[Tuple[int]] = []
        atlantic_cost: List[Tuple[int]] = []
        for r in range(m):
            pacific_cost.append((r, 0))
            falls_into[r][0] += "P"
            atlantic_cost.append((r, n - 1))
            falls_into[r][n - 1] += "A"
        for c in range(n):
            if "P" not in falls_into[0][c]:
                pacific_cost.append((0, c))
                falls_into[0][c] += "P"
            if "A" not in falls_into[m - 1][c]:
                atlantic_cost.append((m - 1, c))
                falls_into[m - 1][c] += "A"
        pacific_queue: deque[Tuple[int]] = deque(pacific_cost)
        atlantic_queue: deque[Tuple[int]] = deque(atlantic_cost)
        # pprint(falls_into)

        # print("Pacific queue")
        while pacific_queue:
            for _ in range(len(pacific_queue)):
                cur_coord = pacific_queue.popleft()
                cur_height = heights[cur_coord[0]][cur_coord[1]]
                for neighbor_r, neighbor_c in get_neighbors(cur_coord):
                    if "P" in falls_into[neighbor_r][neighbor_c]:
                        continue
                    neighbor_height = heights[neighbor_r][neighbor_c]
                    if neighbor_height >= cur_height:
                        falls_into[neighbor_r][neighbor_c] += "P"
                        pacific_queue.append((neighbor_r, neighbor_c))

        result: List[List[int]] = []
        # print("Atlantic queue")
        while atlantic_queue:
            for _ in range(len(atlantic_queue)):
                # print(
                #     f"falls_into[{cur_coord[0]}][{cur_coord[1]}]={falls_into[cur_coord[0]][cur_coord[1]]}"
                # )
                cur_coord = atlantic_queue.popleft()
                cur_height = heights[cur_coord[0]][cur_coord[1]]
                if (
                    "A" in falls_into[cur_coord[0]][cur_coord[1]]
                    and "P" in falls_into[cur_coord[0]][cur_coord[1]]
                ):
                    result.append([cur_coord[0], cur_coord[1]])
                for neighbor_r, neighbor_c in get_neighbors(cur_coord):
                    if "A" in falls_into[neighbor_r][neighbor_c]:
                        continue
                    neighbor_height = heights[neighbor_r][neighbor_c]
                    if neighbor_height >= cur_height:
                        falls_into[neighbor_r][neighbor_c] += "A"
                        atlantic_queue.append((neighbor_r, neighbor_c))

        # pprint(falls_into)

        return result


# @lc code=end
