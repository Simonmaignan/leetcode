#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from typing import Dict


# @lc code=start
class DoubleLinkedNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev: DoubleLinkedNode = None
        self.next: DoubleLinkedNode = None

    def __str__(self) -> str:
        return f"val={self.val} - next={self.next}"


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: Dict[int, int] = {}
        self.least: DoubleLinkedNode = DoubleLinkedNode(-1)
        self.last: DoubleLinkedNode = DoubleLinkedNode(-1)
        self.least.next = self.last
        self.last.prev = self.least
        self.capacity: int = capacity

    def _move_to_last(self, key: int) -> None:
        cur: DoubleLinkedNode = self.least
        while cur.val != key:
            cur = cur.next

        # Unlink cur node from where it is
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        self._add_before_last(cur)

    def _add_before_last(self, node: DoubleLinkedNode) -> None:
        # Add cur node just before last
        node.prev = self.last.prev
        self.last.prev.next = node
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._move_to_last(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._move_to_last(key)
        else:
            node_to_add = DoubleLinkedNode(key)
            self._add_before_last(node_to_add)
            # Over capacity after adding new node
            if len(self.cache) == self.capacity:
                # Remove least used from cache and linked list
                to_remove: DoubleLinkedNode = self.least.next
                del self.cache[to_remove.val]
                # Replace least to point to new least
                self.least.next = to_remove.next
                to_remove.next.prev = self.least
                del to_remove

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
