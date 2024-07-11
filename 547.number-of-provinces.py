#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        is_visited: List[bool] = [False] * n

        def dfs(cur_city: int) -> None:
            # print(f"dfs cur_city={cur_city}")
            is_visited[cur_city] = True
            # print(is_visited)
            for other_city, is_connected in enumerate(isConnected[cur_city]):
                # print(f"other_city={other_city} is_connected={is_connected}")
                if is_connected and not is_visited[other_city]:
                    dfs(other_city)

        nb_provinces = 0
        for cur_city in range(n):
            # print(f"cur_city={cur_city}")
            # print(is_visited)
            if not is_visited[cur_city]:
                nb_provinces += 1
                dfs(cur_city)
            # print(is_visited)

        return nb_provinces


# @lc code=end
