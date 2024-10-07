# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List


def solution(S):
    # Implement your solution here
    cleaned_S: List[str] = []
    for i, S_line in enumerate(S.split("\n")):
        # Header is always clean
        if i == 0:
            cleaned_S.append(S_line)
            continue

        add_line = True
        for S_value in S_line.split(","):
            # Break for this line at the first encountered NULL value
            if S_value == "NULL":
                add_line = False
                break
        # Only keep the clean lines
        if add_line:
            cleaned_S.append(S_line)

    return "\n".join(cleaned_S)
