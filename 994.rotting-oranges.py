#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from typing import Iterator, List, Tuple
from collections import deque


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def get_neighbors(
            cur_cord: Tuple[int, int]
        ) -> Iterator[Tuple[int, int]]:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                new_cord: Tuple[int, int] = tuple(
                    map(sum, zip(cur_cord, direction))
                )
                if 0 <= new_cord[0] < m and 0 <= new_cord[1] < n:
                    yield new_cord

        queue = deque()
        nb_fresh_oranges = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    nb_fresh_oranges += 1

        if not queue:
            if nb_fresh_oranges > 0:
                return -1
            return 0

        nb_minutes = -1
        while queue:
            for _ in range(len(queue)):
                cur_cell_cord = queue.popleft()
                # print(f"cur cell ({cur_cell_cord})={grid[cur_cell_cord[0]][cur_cell_cord[1]]}")
                for neighbor_cord in get_neighbors(cur_cell_cord):
                    if grid[neighbor_cord[0]][neighbor_cord[1]] == 1:
                        # print(f"fresh orange cell ({neighbor_cord})={grid[neighbor_cord[0]][neighbor_cord[1]]}")
                        grid[neighbor_cord[0]][neighbor_cord[1]] = 2
                        queue.append(neighbor_cord)
                        nb_fresh_oranges -= 1
            nb_minutes += 1

        if nb_fresh_oranges > 0:
            return -1

        return nb_minutes


# @lc code=end
