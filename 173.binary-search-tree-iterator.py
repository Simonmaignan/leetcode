#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
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
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator: List[int] = []
        self._dfs(root)
        self.iterator = reversed(self.iterator)

    def _dfs(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        self._dfs(node.left)
        self.iterator.append(node.val)
        self._dfs(node.right)

    def next(self) -> int:
        return self.iterator.pop()

    def hasNext(self) -> bool:
        return len(self.iterator) >= 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
