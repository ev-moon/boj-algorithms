# Problem No. 16234

import sys
from collections import deque

input = sys.stdin.readline

grid_size, L, R = map(int, input().rstrip().split())
population = [list(map(int, input().rstrip().split())) for _ in range(grid_size)]


def BFS(i, j, m_idx):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    length = len(population)
    queue = deque([(i, j)])
    total_pop = population[i][j]
    count = 1
    to_merge = [(i, j)]
    merged[i][j] = m_idx
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in moves:
            nx = cur_x + dx
            ny = cur_y + dy
            if (
                0 <= nx < length
                and 0 <= ny < length
                and merged[nx][ny] == -1
                and L <= abs(population[cur_x][cur_y] - population[nx][ny]) <= R
            ):
                queue.append((nx, ny))
                total_pop += population[nx][ny]
                merged[nx][ny] = m_idx
                to_merge.append((nx, ny))
                count += 1
    avg = total_pop // count
    for ix, iy in to_merge:
        population[ix][iy] = avg


moves = 0
while True:
    merged = [[-1] * grid_size for _ in range(grid_size)]
    m_idx = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if merged[i][j] == -1:  # not merged
                BFS(i, j, m_idx)
                m_idx += 1
    if m_idx == grid_size * grid_size:
        break
    moves += 1

print(moves)