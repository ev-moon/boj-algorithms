# Problem No. 2504

# 76ms
import sys

input = sys.stdin.readline
_input = input().strip()

open_paren = ["(", "["]
point = 1
stack = list()
for char in _input:
    illegal = True  # must re-initialize for each char
    if char in open_paren:
        if point != 1:
            stack.append(point)
        stack.append(char)
    else:
        while stack:
            last = stack.pop()
            if char == ")" and last == "(":
                point *= 2
                stack.append(point)
                point = 1
                illegal = False
                break
            elif char == "]" and last == "[":
                point *= 3
                stack.append(point)
                point = 1
                illegal = False
                break
            elif isinstance(last, int):
                point = min(point + last, point * last)
            else:
                break
        if illegal:  # stop iterating chars when illegal
            break
if illegal:
    print(0)
else:
    try:
        print(sum(stack))
    except:
        print(0)