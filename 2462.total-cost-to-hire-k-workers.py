#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#
from typing import List

# @lc code=start
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        head_candidates_heap: List[int] = costs[:candidates]
        next_head = candidates
        heapq.heapify(head_candidates_heap)
        next_tail = max(candidates, n - candidates)
        tail_candidates_heap: List[int] = costs[-next_tail:]
        next_tail -= 1
        heapq.heapify(tail_candidates_heap)
        # print(head_candidates_heap)
        # print(next_head)
        # print(tail_candidates_heap)
        # print(next_head)
        total_cost = 0
        for _ in range(k):
            # print(f"i={i}")
            if (
                not head_candidates_heap
                or tail_candidates_heap
                and tail_candidates_heap[0] < head_candidates_heap[0]
            ):
                # print("last candidate")
                total_cost += heapq.heappop(tail_candidates_heap)
                # print(total_cost)
                # If there is some candidates left not already in any heap
                if next_head <= next_tail:
                    heapq.heappush(tail_candidates_heap, costs[next_tail])
                    # print(f"last_candidates_heap={last_candidates_heap}")
                    next_tail -= 1
            else:
                # print("first candidate")
                total_cost += heapq.heappop(head_candidates_heap)
                # print(total_cost)
                # If there is some candidates left not already in any heap
                if next_head <= next_tail:
                    heapq.heappush(head_candidates_heap, costs[next_head])
                    # print(f"first_candidates_heap={first_candidates_heap}")
                    next_head += 1

        return total_cost


# @lc code=end
