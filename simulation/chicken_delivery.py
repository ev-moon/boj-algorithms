# Problem No. 15686

from itertools import combinations
import sys

input = sys.stdin.readline

r_size, num_stores = map(int, input().rstrip().split())
houses = []
stores = []
for r_idx in range(r_size):
    row = list(map(int, input().rstrip().split()))
    for c_idx in range(r_size):
        if row[c_idx] == 2:
            stores.append((r_idx, c_idx))
        elif row[c_idx] == 1:
            houses.append((r_idx, c_idx))

answer = float("inf")
for combo in combinations(stores, num_stores):
    total_dist = 0
    for hx, hy in houses:
        house_dist = float("inf")
        for cx, cy in combo:
            house_dist = min(house_dist, abs(hx - cx) + abs(hy - cy))
        total_dist += house_dist
    answer = min(answer, total_dist)
print(answer)