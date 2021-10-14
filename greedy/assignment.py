# Problem No. 13904

import sys

input = sys.stdin.readline

num_assignments = int(input())
assignment_dict = {}
for _ in range(num_assignments):
    deadline, score = map(int, input().strip().split())
    if deadline not in assignment_dict:
        assignment_dict[deadline] = [score]
    else:
        assignment_dict[deadline].append(score)

max_score = 0
available_assignments = []
for day in range(max(assignment_dict.keys()), 0, -1):
    if day in assignment_dict:
        available_assignments.extend(assignment_dict[day])
    if available_assignments:
        cur_max = max(available_assignments)
        max_score += cur_max
        del available_assignments[available_assignments.index(cur_max)]
print(max_score)