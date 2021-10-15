# Problem No. 14888

import sys
from itertools import permutations

input = sys.stdin.readline

_ = input()
numbers = list(map(int, input().strip().split()))
plus, minus, mult, div = map(int, input().strip().split())
op_list = ["+"] * plus + ["-"] * minus + ["*"] * mult + ["/"] * div

max_result = -float("inf")
min_result = float("inf")
cases = set(permutations(op_list))
for combo in cases:
    current_val = numbers[0]
    for idx, op in enumerate(combo):
        if op == "+":
            current_val += numbers[idx + 1]
        elif op == "-":
            current_val -= numbers[idx + 1]
        elif op == "*":
            current_val *= numbers[idx + 1]
        elif op == "/":
            if current_val < 0:
                current_val = -(abs(current_val) // numbers[idx + 1])
            else:
                current_val //= numbers[idx + 1]
    if current_val > max_result:
        max_result = current_val
    if current_val < min_result:
        min_result = current_val
print(max_result)
print(min_result)
