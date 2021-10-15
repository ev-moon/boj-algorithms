# Problem No. 3190

import sys

input = sys.stdin.readline

board_size = int(input().rstrip())
num_apples = int(input().rstrip())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

apples = dict()
for _ in range(num_apples):
    apple_r, apple_c = map(int, input().rstrip().split())
    apple_r -= 1
    apple_c -= 1
    if apple_r not in apples:
        apples[apple_r] = {apple_c}
    else:
        apples[apple_r].add(apple_c)
num_dir_change = int(input().rstrip())
dir_changes = dict()
for _ in range(num_dir_change):
    time, direction = input().rstrip().split()
    dir_changes[int(time)] = direction

cur_dir = 0
cur_coor = [0, 0]
occupied = [(0, 0)]
time = 0
while True:
    time += 1
    cur_coor[0] += dx[cur_dir]
    cur_coor[1] += dy[cur_dir]
    if (
        0 <= cur_coor[0] < board_size
        and 0 <= cur_coor[1] < board_size
        and tuple(cur_coor) not in occupied
    ):  # eligible move
        occupied.append((cur_coor[0], cur_coor[1]))
        if cur_coor[0] in apples and cur_coor[1] in apples[cur_coor[0]]:  # apple
            apples[cur_coor[0]].remove(cur_coor[1])
        else:
            occupied = occupied[1:]
    else:
        break
    if time in dir_changes:
        if dir_changes[time] == "D":
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir + 3) % 4
print(time)
