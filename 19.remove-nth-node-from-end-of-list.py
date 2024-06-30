#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = None
        right = head
        # print(f"right = {right.val}")
        for _ in range(n):
            # print(f"right = {right.val} with next = {right.next}")
            if right is not None:
                right = right.next
        # print(f"right = {right.val}")
        if right is not None:
            left = head
        else:
            return head.next
        # left = head
        # print(f"left = {left.val}")
        while right.next is not None:
            right = right.next
            left = left.next
        # print(f"right = {right.val}")
        # print(f"left = {left.val}")

        left.next = left.next.next

        return head


# @lc code=end
