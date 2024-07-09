#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
from typing import List, Optional


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
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def leaf_value_sequence(
            root: Optional[TreeNode], leaf_value_list: List[int]
        ) -> None:
            if root is None:
                return
            if root.left is None and root.right is None:
                leaf_value_list.append(root.val)
                return
            leaf_value_sequence(root.left, leaf_value_list)
            leaf_value_sequence(root.right, leaf_value_list)

        lvs1 = []
        lvs2 = []
        leaf_value_sequence(root1, lvs1)
        leaf_value_sequence(root2, lvs2)

        return lvs1 == lvs2


# @lc code=end
