def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]) or (A[i + 1] < A[i]):
            return False
    if A[0] != 1 or A[n - 1] != K:
        return False
    else:
        return True


if __name__ == "__main__":
    print(solution([1, 1, 2, 3, 3], 3))
    print(solution([1, 1, 3], 2))
    print(solution([0, 1, 2, 3, 4, 5], 5))
    print(solution([1, 2, 3, 4, 5, 6, 7], 5))
    print(solution([1, 1, 1, 1, 1, 1], 1))
    print(solution([1, 2, 3, 4, 5, 6, 7, 1], 1))
