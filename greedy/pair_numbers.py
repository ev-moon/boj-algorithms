# Problem No. 1744

import sys

input = sys.stdin.readline

positives = []
negatives = []

num_numbers = int(input().strip())

for _ in range(num_numbers):
    num = int(input().strip())
    if abs(num) != num or num == 0:
        negatives.append(num)
    else:
        positives.append(num)

positives.sort()
negatives.sort()
answer = 0
for idx in range(len(positives) - 1, 0, -2):
    answer += max(
        positives[idx] * positives[idx - 1], positives[idx] + positives[idx - 1]
    )
if len(positives) % 2 != 0:
    answer += positives[0]
for idx in range(0, len(negatives) - 1, 2):
    answer += negatives[idx] * negatives[idx + 1]
if len(negatives) % 2 != 0:
    answer += negatives[-1]

print(answer)