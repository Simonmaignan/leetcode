#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#
from collections import deque
from typing import Iterator, List, Tuple


# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def neighbors(cur_coord: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                # new_cord: Tuple[int, int] = tuple(
                #     map(sum, zip(cur_cord, direction))
                # )
                new_cord: Tuple[int, int] = (
                    cur_coord[0] + direction[0],
                    cur_coord[1] + direction[1],
                )
                if 0 <= new_cord[0] < m and 0 <= new_cord[1] < n:
                    yield new_cord

        entrance = (entrance[0], entrance[1])
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = "x"
        nb_steps = 0

        while queue:
            for _ in range(len(queue)):
                cur_coord = queue.pop()
                if cur_coord != entrance and (
                    cur_coord[0] == 0
                    or cur_coord[0] == m - 1
                    or cur_coord[1] == 0
                    or cur_coord[1] == n - 1
                ):
                    return nb_steps
                for neighbor in neighbors(cur_coord):
                    if maze[neighbor[0]][neighbor[1]] == ".":
                        queue.appendleft(neighbor)
                        maze[neighbor[0]][neighbor[1]] = "x"
            nb_steps += 1
        return -1


# @lc code=end
