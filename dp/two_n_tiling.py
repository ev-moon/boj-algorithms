# Problem No. 11726
# DP

import sys

input = sys.stdin.readline


def solution():
    tile_size = int(input().strip())
    answers = [None, 1, 2]
    if tile_size <= 2:
        return answers[tile_size]
    while len(answers) <= tile_size:
        answers.append(answers[-2] + answers[-1])
    return answers[-1]


print(solution() % 10007)
