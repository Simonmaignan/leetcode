#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
from typing import Dict, List, Set, Tuple
from collections import defaultdict, deque


# @lc code=start
# from pprint import pprint


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph: Dict[int, List[Tuple[int, bool]]] = defaultdict(list)
        for city_parent, city_child in connections:
            graph[city_parent].append((city_child, True))
            graph[city_child].append((city_parent, False))
        # pprint(graph)

        visited: Set[int] = set([0])
        queue = deque([0])
        nb_change = 0

        while queue:
            cur_city = queue.popleft()
            for connected_city, wrong_way in graph[cur_city]:
                if connected_city not in visited:
                    visited.add(connected_city)
                    queue.append(connected_city)
                    if wrong_way:
                        nb_change += 1

        return nb_change


# @lc code=end
