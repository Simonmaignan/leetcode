#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.tree_depth = 0
        self.nb_leaf_nodes = 0
        self.nb_nodes = 0
        self.dfs(root, 0)
        if not self.nb_nodes:
            for i in range(self.tree_depth):
                self.nb_nodes += 2**i
            self.nb_nodes += self.nb_leaf_nodes
        return self.nb_nodes

    def dfs(self, node: Optional[TreeNode], node_depth: int) -> None:
        if not node or self.nb_nodes > 0:
            return
        # print(f"node={node.val}")
        self.tree_depth = max(self.tree_depth, node_depth)
        # If node is leaf
        if not node.left and not node.right:
            # print(f"node={node} is leaf")
            if node_depth == self.tree_depth:
                self.nb_leaf_nodes += 1
                # print(f"nb leafs = {self.nb_leaf_nodes}")
            else:
                for i in range(self.tree_depth):
                    self.nb_nodes += 2**i
                self.nb_nodes += self.nb_leaf_nodes
        else:
            self.dfs(node.left, node_depth + 1)
            self.dfs(node.right, node_depth + 1)


# @lc code=end
