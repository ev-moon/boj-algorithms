# Problem No. 5430

import sys

input = sys.stdin.readline

num_cases = int(input().rstrip())

for _ in range(num_cases):
    to_execute = input().rstrip()
    len_array = int(input().rstrip())
    try:
        array = list(map(int, input().rstrip()[1:-1].split(",")))
    except ValueError:
        array = []
    in_order = True
    error = False
    start = 0
    end = len_array
    for char in to_execute:
        if char == "D":
            if in_order:
                start += 1
            else:
                end -= 1
        else:
            in_order = not in_order
        if end < start:
            print("error")
            error = True
            break
    if not error:
        print("[", end="")
        if in_order:
            print(*array[start:end], sep=",", end="")
        else:
            print(*array[start:end][::-1], sep=",", end="")
        print("]")

# 백준풀이

# from sys import stdin
# input = stdin.readline

# for _ in range(int(input())):
#     cmd = input().rstrip()
#     length = int(input())
#     if length:
#         li = list(input()[1:-2].split(','))
#     else:
#         _ = input()
#         li = []

#     Dcount = cmd.count('D')
#     if Dcount > length:
#         print('error')
#         continue
#     elif Dcount == length:
#         print('[]')
#         continue
#     else:
#         Dlist = list(map(len,cmd.split('R')))
#         popLeft = sum(Dlist[0::2])
#         popRight = sum(Dlist[1::2])

#         if popRight:
#             li = li[popLeft:-popRight]
#         else:
#             li = li[popLeft:]

#         if len(Dlist)%2 == 0:
#             li.reverse()
#         print('['+','.join(li)+']')