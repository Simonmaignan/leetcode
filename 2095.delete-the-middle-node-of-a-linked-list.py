#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        fast = slow = prev_slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        if prev_slow is not None and slow is not None:
            prev_slow.next = slow.next

        return head


# @lc code=end
