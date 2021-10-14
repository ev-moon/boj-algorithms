# Problem No. 16236

from collections import deque
import sys

input = sys.stdin.readline
board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]


def solution():
    shark_size = 2
    elapsed_time = 0
    eaten = 0
    for ix in range(board_size):
        for iy in range(board_size):
            if board[ix][iy] == 9:
                shark_coord = (ix, iy)
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    path = deque([[shark_coord, 0]])
    traversed = set()
    possible_coords = []
    while path:
        cur_coord, dist = path.popleft()
        traversed.add((cur_coord))
        for dx, dy in moves:
            nx = cur_coord[0] + dx
            ny = cur_coord[1] + dy
            if (
                0 <= nx < board_size
                and 0 <= ny < board_size
                and (nx, ny) not in traversed
            ):
                if 0 < board[nx][ny] < shark_size:  # eat
                    possible_coords.append((nx, ny))
                    # elapsed_time += dist + 1
                    # path = deque([[(nx, ny), 0]])
                    # traversed = set()
                    # eaten += 1
                    # board[shark_coord[0]][shark_coord[1]] = 0
                    # board[nx][ny] = 9
                    # shark_coord = (nx, ny)
                    # if shark_size == eaten:
                    #     shark_size += 1
                    #     eaten = 0
                    # break
                elif board[nx][ny] in [0, shark_size]:  # pass
                    path.append([(nx, ny), dist + 1])
                    traversed.add((nx, ny))
        if possible_coords and (not path or path[0][1] > dist):
            possible_coords.sort()
            elapsed_time += dist + 1
            nx, ny = possible_coords[0]
            path = deque([[(nx, ny), 0]])
            traversed = set()
            eaten += 1
            board[shark_coord[0]][shark_coord[1]] = 0
            board[nx][ny] = 9
            shark_coord = (nx, ny)
            if shark_size == eaten:
                shark_size += 1
                eaten = 0
            possible_coords = []
    print(elapsed_time)


solution()
