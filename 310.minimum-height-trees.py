#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
from typing import List, Optional, Set, Tuple


# @lc code=start
class Node:
    def __init__(self, value: int, children: Optional[List["Node"]] = None) -> None:
        self.value = value
        if children is None:
            children = []
        self.children = children


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def compute_tree_height(root: int) -> int:
            nodes_created: Set[int] = set([root])

            def dfs(node: int) -> int:
                # print(f"node {node}")
                max_height = 0
                for node1, node2 in edges:
                    if node1 == node and node2 not in nodes_created:
                        nodes_created.add(node2)
                        max_height = max(max_height, dfs(node2) + 1)
                    elif node2 == node and node1 not in nodes_created:
                        nodes_created.add(node1)
                        max_height = max(max_height, dfs(node1) + 1)
                # print(f"node {node}; max_height={max_height}")

                return max_height

            return dfs(root)

        min_height_trees: Tuple[int, List[int]] = (n + 1, [])
        for root in range(n):
            tree_height = compute_tree_height(root)
            # print(f"root {root} tree height = {tree_height}")
            if tree_height < min_height_trees[0]:
                min_height_trees = (tree_height, [root])
            elif tree_height == min_height_trees[0]:
                min_height_trees[1].append(root)

        # print(min_height_trees)
        return min_height_trees[1]


# @lc code=end
