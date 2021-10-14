# Problem No. 18310

num_houses = int(input())

houses = list(map(int, input().split()))
houses.sort()

print(houses[(len(houses) - 1) // 2])
