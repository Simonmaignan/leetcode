#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List, Set


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows: List[Set[int]] = [set() for _ in range(n)]
        columns: List[Set[int]] = [set() for _ in range(n)]
        squares: List[List[Set[int]]] = [
            [set() for _ in range(n)] for _ in range(3)
        ]
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                # print(f"board[{i}][{j}]={num}")
                # print(f"rows[{i}]={rows[i]}")
                # print(f"columns[{j}]={columns[j]}")
                # print(f"squares[{i // 3}][{j // 3}]={squares[i // 3][j // 3]}")
                if (
                    num < 1
                    or num > 9
                    or num in rows[i]
                    or num in columns[j]
                    or num in squares[i // 3][j // 3]
                ):
                    return False
                rows[i].add(num)
                columns[j].add(num)
                squares[i // 3][j // 3].add(num)
                # print(rows)
                # print(columns)
                # print(squares)
                # print(f"rows[{i}]={rows[i]}")
                # print(f"columns[{j}]={columns[j]}")
                # print(f"squares[{i // 3}][{j // 3}]={squares[i // 3][j // 3]}")

        return True


# @lc code=end
