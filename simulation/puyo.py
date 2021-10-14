# Problem No. 11559

import sys

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]  # 12-line field
width = len(board[0])
length = len(board)
iterations = 0


def pop_block(start_x, start_y, board):
    traversed = set()
    traversed.add((start_x, start_y))
    stack = [(start_x, start_y)]
    to_pop = [(start_x, start_y)]
    color = board[start_x][start_y]
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while stack:
        x, y = stack.pop()
        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy
            if (
                0 <= new_x < length
                and 0 <= new_y < width
                and (new_x, new_y) not in traversed
            ):
                traversed.add((new_x, new_y))
                if board[new_x][new_y] == color:
                    stack.append((new_x, new_y))
                    to_pop.append((new_x, new_y))
    return to_pop


while True:
    pop = False
    for row in range(length):
        for col in range(width):
            if board[row][col] != ".":
                match = pop_block(row, col, board)
                if len(match) >= 4:
                    pop = True
                    for (r_idx, c_idx) in match:
                        board[r_idx][c_idx] = "."
    if not pop:
        break
    # pop and update board
    for j in range(width):
        for i in range(length - 2, -1, -1):
            if board[i][j] != ".":
                for n_idx in range(i + 1, length):
                    if board[n_idx][j] != ".":
                        break
                    board[n_idx][j] = board[n_idx - 1][j]
                    board[n_idx - 1][j] = "."
    iterations += 1

print(iterations)
