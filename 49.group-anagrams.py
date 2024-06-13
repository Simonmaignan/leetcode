#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import Dict, List


# @lc code=start
# from pprint import pprint


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict: Dict[str, List[str]] = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        # pprint(anagram_dict)

        ans: List[List[str]] = [
            anagram_list for _, anagram_list in anagram_dict.items()
        ]
        # print(ans)
        return ans


# @lc code=end
