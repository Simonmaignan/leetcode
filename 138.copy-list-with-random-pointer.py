#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        dummy = Node(0)
        cur_orig = head
        cur_copy = dummy
        # Build new list without random
        while cur_orig:
            new_copy = Node(cur_orig.val)
            cur_copy.next = new_copy
            cur_copy = cur_copy.next
            cur_orig = cur_orig.next

        # Point to random
        cur_orig = head
        cur_copy = dummy.next
        while cur_orig:
            if cur_orig.random:
                random_copy = dummy.next
                random_orig = head
                while random_orig != cur_orig.random:
                    random_orig = random_orig.next
                    random_copy = random_copy.next
                cur_copy.random = random_copy
            cur_copy = cur_copy.next
            cur_orig = cur_orig.next

        return dummy.next


# @lc code=end
