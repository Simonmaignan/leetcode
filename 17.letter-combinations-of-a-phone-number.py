#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import Dict, List


# @lc code=start
class Solution:
    digit2letter: Dict[str, str] = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        letters_combinations: List[str] = []
        n = len(digits)

        # print(n)
        def dfs(idx: int, letters_combination: List[str]) -> None:
            # print(f"idx={idx}")
            if idx == n:
                letters_combinations.append("".join(letters_combination))
                # print(letters_combinations)
                return
            digit = digits[idx]
            # print(f"digit={digit}")
            for letter in self.digit2letter[digit]:
                letters_combination.append(letter)
                dfs(idx + 1, letters_combination)
                letters_combination.pop()

        if n == 0:
            return []
        dfs(0, [])
        return letters_combinations


# @lc code=end
