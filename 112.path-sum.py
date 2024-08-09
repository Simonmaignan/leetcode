#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], cur_sum: int) -> bool:
            if node is None:
                return False

            cur_sum += node.val
            # print(f"node={node.val}; sum={cur_sum}")
            # If is leaf and current sum equals to target sum
            if (
                node.left is None
                and node.right is None
                and cur_sum == targetSum
            ):
                return True

            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)


# @lc code=end
