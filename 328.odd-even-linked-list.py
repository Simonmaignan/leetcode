#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node: Optional[ListNode] = head
        if head is None or head.next is None:
            return head
        even_node: Optional[ListNode] = head.next
        even_list_root = ListNode(next=even_node)
        while even_node is not None and even_node.next is not None:
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next
            even_node.next = even_node.next.next
            even_node = even_node.next
        odd_node.next = even_list_root.next

        return head


# @lc code=end
