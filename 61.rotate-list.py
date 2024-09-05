#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
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
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        k %= n
        print(f"k={k}; n={n}")
        if k == 0:
            return head
        i = 0
        cur = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while cur.next:
            if i < (n - k):
                prev = prev.next
            elif i == n - k:
                prev.next = None
                head = cur
            i += 1
            cur = cur.next
        if k == 1:
            prev.next = None
            head = cur
        cur.next = dummy.next
        return head


# @lc code=end
