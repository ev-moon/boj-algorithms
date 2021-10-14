# Problem No. 1300

import sys

input = sys.stdin.readline


def solution():
    length = int(input())
    target = int(input())
    low, high = 1, target
    answer = low
    while low <= high:
        mid = (low + high) // 2
        num_smaller_elements = sum(
            [min(mid // idx, length) for idx in range(1, length + 1)]
        )
        if num_smaller_elements >= target:
            answer = mid
            high = mid - 1
        elif num_smaller_elements < target:
            low = mid + 1
    return answer


print(solution())