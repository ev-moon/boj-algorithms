# Problem No. 18405

from collections import deque
import sys

input = sys.stdin.readline

g_size, num_virus = map(int, input().rstrip().split())
grid = [list(map(int, input().split())) for _ in range(g_size)]
spread_time, x, y = map(int, input().split())

queue = []
for i in range(g_size):
    for j in range(g_size):
        if grid[i][j] != 0:
            queue.append((grid[i][j], 0, i, j))
queue.sort()
queue = deque(queue)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    virus, time, cx, cy = queue.popleft()
    if time == spread_time:
        break
    for dx, dy in moves:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < g_size and 0 <= ny < g_size and grid[nx][ny] == 0:
            grid[nx][ny] = virus
            queue.append((virus, time + 1, nx, ny))

print(grid[x - 1][y - 1])
