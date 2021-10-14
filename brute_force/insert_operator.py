# Problem No. 14888

import sys
from itertools import permutations

input = sys.stdin.readline

n_numbers = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
n_ops = list(map(int, input().rstrip().split()))
operators = "+" * n_ops[0] + "-" * n_ops[1] + "*" * n_ops[2] + "/" * n_ops[3]
max_result = float("-inf")
min_result = float("inf")

cases = set(permutations(operators))
for combo in cases:
    mid = numbers[0]
    for op, num in zip(combo, numbers[1:]):
        if op == "+":
            mid += num
        elif op == "-":
            mid -= num
        elif op == "*":
            mid *= num
        else:
            if mid < 0:
                mid = -(abs(mid) // num)
            else:
                mid //= num
    max_result = max(mid, max_result)
    min_result = min(mid, min_result)

print(max_result)
print(min_result)
