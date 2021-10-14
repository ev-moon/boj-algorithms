# Problem No. 14502
# Brute Force + BFS

import sys

input = sys.stdin.readline

v_len, h_len = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(v_len)]
temp = [[0] * h_len for _ in range(v_len)]

max_safe_blocks = 0


def count_safe_blocks(grid):
    num_safe_blocks = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                num_safe_blocks += 1
    return num_safe_blocks


def expand(start):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in moves:
        nx = start[0] + dx
        ny = start[1] + dy
        if 0 <= nx < v_len and 0 <= ny < h_len:  # possible move
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                expand((nx, ny))


def dfs(count):
    global max_safe_blocks
    if count == 3:
        for x in range(v_len):
            for y in range(h_len):
                temp[x][y] = grid[x][y]
        for idx_x in range(v_len):
            for idx_y in range(h_len):
                if temp[idx_x][idx_y] == 2:
                    expand((idx_x, idx_y))
        max_safe_blocks = max(count_safe_blocks(temp), max_safe_blocks)
        return
    for i in range(v_len):
        for j in range(h_len):
            if grid[i][j] == 0:
                grid[i][j] = 1
                count += 1
                dfs(count)
                grid[i][j] = 0
                count -= 1


dfs(0)
print(max_safe_blocks)