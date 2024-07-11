#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_path_value: int) -> int:
            if node is None:
                return 0
            nb_good_nodes = 0
            if node.val >= max_path_value:
                max_path_value = node.val
                nb_good_nodes += 1
            nb_good_nodes += dfs(node.left, max_path_value)
            nb_good_nodes += dfs(node.right, max_path_value)
            return nb_good_nodes

        return dfs(root, -(10**4) - 1)


# @lc code=end
