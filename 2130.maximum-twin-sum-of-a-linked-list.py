#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        linked_list: List[int] = []
        while head:
            linked_list.append(head.val)
            head = head.next
        max_twin_sum = 0
        for i in range(len(linked_list) // 2 + 1):
            max_twin_sum = max(
                max_twin_sum, linked_list[i] + linked_list[-(i + 1)]
            )

        return max_twin_sum


# @lc code=end
