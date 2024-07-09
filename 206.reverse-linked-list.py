#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import List, Optional


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
        # if head is None:
        #     return None
        # if head.next is None:
        #     return head
        # new_node = self.reverseList(head.next)
        # new_node.next = head
        # return new_node
        nodes_list: List[ListNode] = []
        while head:
            nodes_list.append(head)
            head = head.next

        if not nodes_list:
            return None

        reversed_list_first: ListNode = nodes_list.pop()
        reversed_list: ListNode = reversed_list_first
        while nodes_list:
            reversed_list.next = nodes_list.pop()
            reversed_list = reversed_list.next
        reversed_list.next = None

        return reversed_list_first


# @lc code=end
