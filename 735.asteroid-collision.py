#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
from typing import List


# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []

        for asteroid in asteroids:
            enters_stack = True
            # We have a collision
            while stack and stack[-1] > 0 and asteroid < 0:
                # Left going is bigger -> Right is destroyed
                if stack[-1] < -asteroid:
                    stack.pop()
                # Same size -> Right is destroyed and left not entering stack
                elif stack[-1] == -asteroid:
                    stack.pop()
                    enters_stack = False
                    break
                # Right going is bigger -> Left going does not enter the stack
                else:
                    enters_stack = False
                    break
            if enters_stack:
                stack.append(asteroid)

        return stack


# @lc code=end
