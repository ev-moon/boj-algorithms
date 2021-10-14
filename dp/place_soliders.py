# Problem No. 18353

N = int(input().rstrip())
atk_list = list(map(int, input().rstrip().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if atk_list[j] > atk_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
