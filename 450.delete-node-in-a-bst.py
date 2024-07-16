#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if node.val == key:
                _del_node(node)

            elif node.val < key:
                dfs(node.right)
            else:
                dfs(node.left)

        def _del_node(node: TreeNode) -> None:
            if not node.left and not node.right:
                node = None
                return
            if not node.left or not node.right:
                node = node.left if node.left else node.right
                return
            # Both node.left and node.right
            in_order_successor: TreeNode = node.right
            while in_order_successor.left:
                in_order_successor = in_order_successor.left
            node.val = in_order_successor.val
            in_order_successor = None

        dfs(root)
        return root


# @lc code=end
