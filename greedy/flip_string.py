# Problem No. 1439

import sys

input = sys.stdin.readline

string = input().rstrip()
start_zero = string[0] == "0"
answer = [0, 1] if start_zero else [1, 0]
for idx, char in enumerate(string[1:]):
    if char != string[idx]:
        if char == "0":
            answer[1] += 1
        else:
            answer[0] += 1

print(min(answer))