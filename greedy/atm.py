# Problem No. 11399

import sys

input = sys.stdin.readline

num_ppl = int(input().strip())
time_needed = list(map(int, input().strip().split()))
time_needed.sort()

idx = 0
total_time = 0
while idx < num_ppl:
    total_time += (num_ppl - idx) * time_needed[idx]
    idx += 1
print(total_time)
