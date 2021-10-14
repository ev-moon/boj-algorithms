# Problem No. 13459

import sys
from collections import deque


def move_marble(board, cur_r, cur_c, dr, dc):
    while board[cur_r + dr][cur_c + dc] != "#" and board[cur_r][cur_c] != "O":
        cur_r += dr
        cur_c += dc
    return (cur_r, cur_c)


input = sys.stdin.readline

num_r, num_c = map(int, input().split())

# Construct board and positions
board = [list(input().strip()) for _ in range(num_r)]
for i in range(num_r):
    for j in range(num_c):
        if board[i][j] == "R":
            red_pos = (i, j)
        elif board[i][j] == "B":
            blue_pos = (i, j)

positions = set([(red_pos + blue_pos)])
queue = deque([[red_pos, blue_pos, 1]])  # depth == 1: main gotcha!
while queue:
    cur_red, cur_blue, cur_moves = queue.popleft()
    if cur_moves > 10:
        break
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move in moves:  # up, down, left, right
        red_r, red_c = move_marble(board, cur_red[0], cur_red[1], move[0], move[1])
        blue_r, blue_c = move_marble(board, cur_blue[0], cur_blue[1], move[0], move[1])
        if board[blue_r][blue_c] == "O":
            continue
        if board[red_r][red_c] == "O":  # success
            print(1)
            sys.exit(0)
        if (red_r, red_c) == (blue_r, blue_c):  # adjust if overlap
            red_dist = abs(red_r - cur_red[0]) + abs(red_c - cur_red[1])
            blue_dist = abs(blue_r - cur_blue[0]) + abs(blue_c - cur_blue[1])
            if red_dist > blue_dist:
                red_r -= move[0]
                red_c -= move[1]
            else:
                blue_r -= move[0]
                blue_c -= move[1]
        if (red_r, red_c, blue_r, blue_c) not in positions:
            positions.add((red_r, red_c, blue_r, blue_c))
            queue.append([(red_r, red_c), (blue_r, blue_c), cur_moves + 1])
print(0)
