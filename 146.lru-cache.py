#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from typing import Dict


# @lc code=start
class DoubleLinkedNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev: DoubleLinkedNode = None
        self.next: DoubleLinkedNode = None

    def __str__(self) -> str:
        return f"key={self.key}; val={self.val}; next={self.next}"


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: Dict[int, DoubleLinkedNode] = {}
        self.least: DoubleLinkedNode = DoubleLinkedNode(-1, -1)
        self.last: DoubleLinkedNode = DoubleLinkedNode(-1, -1)
        self.least.next = self.last
        self.last.prev = self.least
        self.capacity: int = capacity

    def _move_to_last(self, key: int) -> None:
        # Unlink cur node from where it is
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev

        self._add_before_last(self.cache[key])

    def _add_before_last(self, node: DoubleLinkedNode) -> None:
        # Add cur node just before last
        node.prev = self.last.prev
        self.last.prev.next = node
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._move_to_last(key)
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._move_to_last(key)
            self.cache[key].val = value
        else:
            node_to_add = DoubleLinkedNode(key, value)
            self._add_before_last(node_to_add)
            self.cache[key] = node_to_add
            # Over capacity after adding new node
            if len(self.cache) > self.capacity:
                # Remove least used from cache and linked list
                to_remove: DoubleLinkedNode = self.least.next
                # Replace least to point to new least
                self.least.next = to_remove.next
                to_remove.next.prev = self.least
                del self.cache[to_remove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
