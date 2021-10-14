# Problem No. 11047

# 1. DP: Memory Exceed
# import sys

# input = sys.stdin.readline

# num_coins, target_sum = map(int, input().strip().split())
# coins = set()

# for _ in range(num_coins):
#     coins.add(int(input().strip()))

# dp = [float("inf")] * (target_sum + 1)

# for c_sum in range(len(dp)):
#     if c_sum in coins:
#         dp[c_sum] = 1
#     else:
#         for coin in coins:
#             if c_sum - coin > 0:
#                 dp[c_sum] = min(dp[c_sum], dp[c_sum - coin] + 1)
# print(dp[-1])


# 2. Greedy

import sys

input = sys.stdin.readline

num_coins, target_sum = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(num_coins)]
answer = 0

for idx in range(-1, -(num_coins + 1), -1):
    coins_used, target_sum = divmod(target_sum, coins[idx])
    answer += coins_used
    if target_sum == 0:
        break

print(answer)