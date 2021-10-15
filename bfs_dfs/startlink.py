# Problem No. 5014

import sys
from collections import deque

input = sys.stdin.readline

num_floors, cur_floor, dest_floor, up_unit, down_unit = map(
    int, input().strip().split()
)


traversed = set()
queue = deque([(cur_floor, 0)])
while queue:
    floor_pointer, pushes = queue.popleft()
    if floor_pointer == dest_floor:
        print(pushes)
        sys.exit(0)
    if floor_pointer not in traversed:
        traversed.add(floor_pointer)
        temp_up = floor_pointer + up_unit
        if temp_up <= num_floors and temp_up not in traversed:
            queue.append((temp_up, pushes + 1))
        temp_down = floor_pointer - down_unit
        if temp_down > 0 and temp_down not in traversed:
            queue.append((temp_down, pushes + 1))
print("use the stairs")
