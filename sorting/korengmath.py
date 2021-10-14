# Problem No. 10825

import sys

input = sys.stdin.readline

num_students = int(input().rstrip())
score_list = []

for _ in range(num_students):
    name, kor, eng, math = input().rstrip().split()
    score_list.append((-int(kor), int(eng), -int(math), name))

score_list.sort()
print(*[item[3] for item in score_list], sep="\n")
