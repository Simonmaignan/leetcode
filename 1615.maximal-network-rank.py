#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#
from collections import defaultdict
from typing import Dict, List, Set


# @lc code=start
# from pprint import pprint


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cities_graph: Dict[int, Set[int]] = defaultdict(set)

        for city_a, city_b in roads:
            cities_graph[city_a].add(city_b)
            cities_graph[city_b].add(city_a)

        # pprint(cities_graph)
        max_rank = 0
        for city_1 in range(n):
            for city_2 in range(city_1 + 1, n):
                connected_cities: int = len(cities_graph[city_1]) + len(
                    cities_graph[city_2]
                )
                if city_2 in cities_graph[city_1]:
                    connected_cities -= 1
                # print(f"rank ({city_1}, {city_2}) = {cities_con}")
                max_rank = max(max_rank, connected_cities)

        return max_rank


# @lc code=end
