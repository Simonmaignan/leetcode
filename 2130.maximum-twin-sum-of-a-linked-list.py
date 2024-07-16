#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy_node = ListNode()
        cur_node = head
        n = 0
        while cur_node:
            n += 1
            next_node: ListNode = cur_node.next
            cur_node.next = dummy_node.next
            dummy_node.next = cur_node
            cur_node = next_node

        cur_node = head
        cur_reversed_node = dummy_node.next
        print(cur_node)
        print(cur_reversed_node)
        max_twin_sum = 0
        for _ in range(n // 2 + 1):
            max_twin_sum = max(
                max_twin_sum, cur_node.val + cur_reversed_node.val
            )
            cur_node = cur_node.next
            cur_reversed_node = cur_reversed_node.next

        return max_twin_sum


# @lc code=end
