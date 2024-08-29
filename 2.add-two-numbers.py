#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            d1 = d2 = 0
            if l1:
                d1 = l1.val
            if l2:
                d2 = l2.val
            carry, d_add = divmod(d1 + d2 + carry, 10)
            l_add = ListNode(val=d_add)
            cur.next = l_add
            cur = l_add
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# @lc code=end
