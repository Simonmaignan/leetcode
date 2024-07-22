#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
from typing import Dict


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
        memo: Dict[int, bool] = {}

        def isChild(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> bool:
            if root is None:
                return False
            if root.val in memo:
                return memo[root.val]
            if root.val == p.val or root.val == q.val:
                return True
            is_child = isChild(root.left, p, q) or isChild(root.right, p, q)
            memo[root.val] = is_child
            return is_child

        if root is None:
            return None
        is_left_child = (
            root.val == p.val or root.val == q.val or isChild(root.left, p, q)
        )
        is_right_child = (
            root.val == p.val or root.val == q.val or isChild(root.right, p, q)
        )
        if is_left_child and is_right_child:
            return root
        if is_left_child:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


# @lc code=end
