from typing import List


def solution(S: str) -> int:
    n = len(S)
    # Transform into list since string is immutable
    s_list: List[str] = list(S)

    # Count leading 0s
    leading_0s = 0
    while leading_0s < n and s_list[leading_0s] == "0":
        leading_0s += 1

    nb_op = 0
    # Until were're before last non leading 0 bit
    while len(s_list) > leading_0s + 1:
        lsb: str = s_list.pop()
        # Divide by 2
        if lsb == "0":
            nb_op += 1
        # Minus 1 then divide by 2
        else:
            nb_op += 2
    # Minus 1
    if s_list[-1] == "1":
        nb_op += 1

    return nb_op


if __name__ == "__main__":
    s = "".join(["1" for _ in range(400000)])
    print(solution(s))
