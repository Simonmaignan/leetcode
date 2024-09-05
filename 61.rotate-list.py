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
        # print(f"k={k}; n={n}")
        if k == 0:
            return head

        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None

        return head


# @lc code=end
