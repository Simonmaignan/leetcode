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
        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        if not root.left or not root.right:
            root = root.left if root.left else root.right
            return root
        # Both node.left and node.right
        in_order_successor: TreeNode = root.right
        while in_order_successor.left:
            in_order_successor = in_order_successor.left
        root.val = in_order_successor.val
        root.right = self.deleteNode(root.right, in_order_successor.val)

        return root


# @lc code=end
