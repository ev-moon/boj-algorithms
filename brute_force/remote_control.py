# Problem No. 1107
import sys

channel = int(input())
num_broken = int(input())

answer = abs(channel - 100)
if num_broken == 0:
    print(min(answer, len(str(channel))))
    sys.exit(0)

to_exclude = list(map(int, input().split()))


def check_reachable(number):
    num_array = list(map(int, list(str(number))))
    for num in num_array:
        if num in to_exclude:
            return False
    return True


for num in range(1000000):
    if check_reachable(num):
        answer = min(answer, abs(channel - num) + len(str(num)))

print(answer)
