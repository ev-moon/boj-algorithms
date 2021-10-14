# Problem No. 14501

import sys

input = sys.stdin.readline

num_days = int(input().rstrip())

schedule = [tuple(map(int, input().rstrip().split())) for _ in range(num_days)]
dp = [0] * (num_days + 1)
max_profit = 0

for i in range(num_days - 1, -1, -1):
    days, profit = schedule[i]
    if i + days <= num_days:
        dp[i] = max(dp[i + days] + profit, max_profit)
        max_profit = dp[i]
    else:
        dp[i] = max_profit

print(max_profit)