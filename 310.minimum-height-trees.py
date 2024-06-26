#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
from typing import Dict, List
from collections import defaultdict, deque


# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        node_relations: Dict[int, List[int]] = defaultdict(list)
        nodes_indegree: List[int] = [0] * n
        for node1, node2 in edges:
            node_relations[node1].append(node2)
            nodes_indegree[node1] += 1
            node_relations[node2].append(node1)
            nodes_indegree[node2] += 1

        nodes_layer: deque[int] = deque()
        for node, node_indegree in enumerate(nodes_indegree):
            if node_indegree == 1:
                nodes_layer.append(node)

        ans: List[int] = []
        while nodes_layer:
            ans.clear()
            for _ in range(len(nodes_layer)):
                cur_node = nodes_layer.popleft()
                ans.append(cur_node)
                for connected_node in node_relations[cur_node]:
                    nodes_indegree[connected_node] -= 1
                    if nodes_indegree[connected_node] == 1:
                        nodes_layer.append(connected_node)

        return ans


# @lc code=end
