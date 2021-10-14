# Problem No. 2178

from collections import deque
import sys

input = sys.stdin.readline

# construct maze
num_row, num_col = map(int, input().strip().split())
maze = []
for _ in range(num_row):
    maze.append(list(input().strip()))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

traversed = set()
start = (0, 0)
queue = deque([[start, 1]])
while True:
    cur_coord, dist = queue.popleft()
    if cur_coord not in traversed:
        if cur_coord == (num_row - 1, num_col - 1):
            break
        traversed.add(cur_coord)
        cur_x, cur_y = cur_coord
        for move in moves:
            n_x = cur_x + move[0]
            n_y = cur_y + move[1]
            if (
                0 <= n_x < num_row
                and 0 <= n_y < num_col
                and (n_x, n_y) not in traversed
            ):  # valid move
                if maze[n_x][n_y] == "1":
                    queue.append([(n_x, n_y), dist + 1])
print(dist)