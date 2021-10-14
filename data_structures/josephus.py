# Question No. 1158

import sys

input = sys.stdin.readline
n_people, step = map(int, input().split())

# Time Over
# removed = set([step])
# print("<{}".format(step), end="")
# pointer = step
# remaining_steps = step
# while len(removed) < n_people:
#     while remaining_steps > 0:
#         while pointer+1 in removed or pointer == n_people:
#             if pointer == n_people:
#                 pointer = 0
#             else:
#                 pointer +=1
#         pointer +=1
#         remaining_steps -=1
#     removed.add(pointer)
#     print(", {}".format(pointer), end="")
#     remaining_steps = step
# print(">")

# Correct 76ms
remaining = [i+1 for i in range(n_people)]
pointer = step - 1
print("<{}".format(remaining[pointer]), end="")
del remaining[pointer]
while remaining:
    pointer = (pointer + step-1)%len(remaining)
    print(", {}".format(remaining[pointer]), end="")
    del remaining[pointer]

print(">")