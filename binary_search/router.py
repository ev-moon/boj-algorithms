# Problem No. 2110

import sys

input = sys.stdin.readline


def traverse(houses, min_dist, num_routers):
    cur_dist = float("inf")
    cur_idx = 0
    installed = 1
    while cur_idx < len(houses) - 1:

        n_idx = cur_idx + 1
        while n_idx < len(houses) - 1 and houses[n_idx] - houses[cur_idx] < min_dist:
            n_idx += 1
        if houses[n_idx] - houses[cur_idx] >= min_dist:
            installed += 1
            cur_dist = min(cur_dist, houses[n_idx] - houses[cur_idx])
            cur_idx = n_idx
            if installed == num_routers:
                return cur_dist
        else:
            break
    return -1


num_houses, num_routers = map(int, input().rstrip().split())

houses = [int(input().rstrip()) for _ in range(num_houses)]
houses.sort()

right = houses[-1] - houses[0]
left = answer = 1
while left <= right:
    mid = (left + right) // 2
    traverse_dist = traverse(houses, mid, num_routers)
    if traverse_dist == -1:
        right = mid - 1
    else:
        answer = traverse_dist
        left = traverse_dist + 1
print(answer)