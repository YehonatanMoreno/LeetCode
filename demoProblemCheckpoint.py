from typing import List


def Solution(A: List[int]):
    n = len(A)
    counter = {i: 0 for i in range(1, n + 1)}
    for num in A:
        if num in counter:
            counter[num] += 1
    for num in counter:
        if counter[num] == 0:
            return num
    return n + 1
    