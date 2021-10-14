# Problem No. 2696

import sys

input = sys.stdin.readline

t_cases = int(input().strip())

for it in range(t_cases):
    size = int(input().strip())
    numbers = list()
    print(size // 2 + 1)
    while len(numbers) < size:
        for num in map(int, input().strip().split()):
            numbers.append(num)
            if len(numbers) % 2 == 1:
                numbers.sort()
                print(numbers[len(numbers) // 2], end=" ")
                if len(numbers) % 20 == 19:
                    print("")
    print("")
