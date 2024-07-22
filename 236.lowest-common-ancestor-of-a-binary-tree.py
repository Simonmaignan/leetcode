#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.p_path: List[TreeNode] = []
        self.q_path: List[TreeNode] = []

        def dfs(
            node: Optional["TreeNode"], current_path: List["TreeNode"]
        ) -> None:
            if node is None:
                return
            # Both q and p have been found
            if self.p_path and self.q_path:
                return

            if node == p:
                self.p_path = current_path[:]

            if node == q:
                self.q_path = current_path[:]

            current_path.append(node.left)
            dfs(node.left, current_path)
            current_path.pop()

            current_path.append(node.right)
            dfs(node.right, current_path)
            current_path.pop()

        dfs(root, [root])

        n_p = len(self.p_path)
        n_q = len(self.q_path)
        i = max(n_p, n_q) - 1
        while i >= 0:
            if i >= n_p or i >= n_q:
                i -= 1
            elif self.p_path[i] == self.q_path[i]:
                return self.p_path[i]
            else:
                i -= 1


# @lc code=end
