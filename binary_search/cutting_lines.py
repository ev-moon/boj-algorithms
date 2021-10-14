# Problem No. 1654

import sys

input = sys.stdin.readline


def solution():
    num_lines, target_number = map(int, input().split())
    lines = sorted([int(input()) for _ in range(num_lines)], reverse=True)
    low, hi = max(1, lines[0] // target_number), sum(lines) // target_number
    answer = low
    while low <= hi:
        mid = (low + hi) // 2
        curr_lines = 0
        for line in lines:
            curr_lines += line // mid
            if curr_lines >= target_number:
                answer = mid
                low = mid + 1
                break
        if curr_lines < target_number:
            hi = mid - 1
    return answer


print(solution())
