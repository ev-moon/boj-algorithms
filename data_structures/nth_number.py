# Problem No. 2075

import sys

input = sys.stdin.readline

n = int(input().strip())
stack = list()

for it in range(n):
    stack.extend(map(int, input().strip().split()))
    stack.sort()
    if len(stack) > n:
        stack = stack[n:]

print(stack[0])