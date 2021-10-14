# Problem No. 17144

import sys
import copy

input = sys.stdin.readline

num_r, num_c, time = map(int, input().split())
room = [list(map(int, input().strip().split())) for _ in range(num_r)]
for idx in range(num_r):
    if room[idx][0] == -1:
        cir_pos = (idx, idx + 1)
        break


def spread():
    room_copy = copy.deepcopy(room)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for ridx in range(num_r):
        for cidx in range(num_c):
            if room[ridx][cidx] >= 5:
                for dx, dy in moves:
                    nx, ny = ridx + dx, cidx + dy
                    if 0 <= nx < num_r and 0 <= ny < num_c and room[nx][ny] != -1:
                        room_copy[nx][ny] += room[ridx][cidx] // 5
                        room_copy[ridx][cidx] -= room[ridx][cidx] // 5
    return room_copy


def circulate():
    room_copy = copy.deepcopy(room)
    # upper half
    room_copy[cir_pos[0]][1], room_copy[cir_pos[1]][1] = 0, 0
    for c_idx in range(2, num_c):
        room_copy[cir_pos[0]][c_idx] = room[cir_pos[0]][c_idx - 1]
    for r_idx in range(cir_pos[0] - 1, -1, -1):
        room_copy[r_idx][-1] = room[r_idx + 1][-1]
    for c_idx in range(num_c - 2, -1, -1):
        room_copy[0][c_idx] = room[0][c_idx + 1]
    for r_idx in range(1, cir_pos[0]):
        room_copy[r_idx][0] = room[r_idx - 1][0]
    # lower half
    for c_idx in range(2, num_c):
        room_copy[cir_pos[1]][c_idx] = room[cir_pos[1]][c_idx - 1]
    for r_idx in range(cir_pos[1] + 1, num_r):
        room_copy[r_idx][-1] = room[r_idx - 1][-1]
    for c_idx in range(num_c - 2, -1, -1):
        room_copy[-1][c_idx] = room[-1][c_idx + 1]
    for r_idx in range(num_r - 2, cir_pos[1], -1):
        room_copy[r_idx][0] = room[r_idx + 1][0]
    return room_copy


for _ in range(time):
    room = spread()
    room = circulate()
print(sum([sum(row) for row in room]) + 2)

# Case 1
# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0
# Answer: 188