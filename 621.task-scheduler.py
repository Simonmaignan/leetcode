#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from typing import Dict, List
from collections import Counter, defaultdict

# @lc code=start
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task_next_cycle: Dict[str, int] = defaultdict(int)
        heap: List[int, str] = []
        task_counter = Counter(tasks)

        for task, task_nb in task_counter.items():
            heapq.heappush(heap, (0, task_nb, task))
            # task_next_cycle[task] += n

        nb_cycles = 0

        while heap:
            next_cycle, task_nb, task = heapq.heappop(heap)
            print(
                f"task = {task}; next_cycle = {next_cycle}; task_nb = {task_nb}; nb_cycle = {nb_cycles}"
            )
            while nb_cycles < next_cycle:
                nb_cycles += 1
            nb_cycles += 1
            print(f"nb_cycle = {nb_cycles}")

            task_nb -= 1
            if task_nb > 0:
                heapq.heappush(heap, (nb_cycles + n, task_nb, task))

        return nb_cycles


# @lc code=end
