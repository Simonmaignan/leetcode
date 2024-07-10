#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
from typing import List, Set


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: Set[int] = set()
        n = len(rooms)

        def visit(room: int) -> None:
            if room in visited:
                return
            visited.add(room)

            for key in rooms[room]:
                visit(key)

        visit(0)
        return len(visited) == n


# @lc code=end
