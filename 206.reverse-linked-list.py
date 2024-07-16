#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = dummy_node.next
            dummy_node.next = cur_node
            cur_node = next_node
        return dummy_node.next


# @lc code=end
