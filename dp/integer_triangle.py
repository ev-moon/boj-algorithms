# Problem No. 1932

import sys

input = sys.stdin.readline

size = int(input().rstrip())
triangle = [list(map(int, input().rstrip().split())) for _ in range(size)]

dp = []
for row in triangle:
    row_best = []
    for idx, element in enumerate(row):
        if not dp:
            row_best = [element]
        else:
            if idx == 0:
                row_best.append(dp[-1][0] + element)
            elif idx == len(row) - 1:
                row_best.append(dp[-1][-1] + element)
            else:
                row_best.append(max(dp[-1][idx - 1], dp[-1][idx]) + element)
    dp.append(row_best)

print(max(dp[-1]))