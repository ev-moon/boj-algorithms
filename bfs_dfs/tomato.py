# Problem No. 7569

import sys
from collections import deque

input = sys.stdin.readline


def BFS(queue):
    num_days = 0
    moves = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    while queue:
        for _ in range(len(queue)):
            new_ripe_idx = queue.popleft()
            for move in moves:
                new_h, new_w, new_l = [
                    item1 + item2 for item1, item2 in zip(new_ripe_idx, move)
                ]
                if 0 <= new_h < height and 0 <= new_w < width and 0 <= new_l < length:
                    if tomato_crates[new_h][new_w][new_l] == 0:
                        tomato_crates[new_h][new_w][new_l] = 1
                        queue.append((new_h, new_w, new_l))
        num_days += 1
    return num_days - 1


length, width, height = map(int, input().strip().split())
tomato_crates = [
    [list(map(int, input().split())) for _ in range(width)] for _ in range(height)
]
wave = deque([])

for n_h in range(height):
    for n_w in range(width):
        for n_l in range(length):
            if tomato_crates[n_h][n_w][n_l] == 1:
                wave.appendleft((n_h, n_w, n_l))

if len(wave) == length * width * height:
    print(0)
    exit()

num_days = BFS(wave)
for x in range(height):
    for y in range(width):
        for z in range(length):
            if tomato_crates[x][y][z] == 0:
                print(-1)
                exit()

print(num_days)
