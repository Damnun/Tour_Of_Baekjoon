n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    for j in range(k + 1):
        if j - coins[i] >= 0:
            dp[j] += dp[j - coins[i]]
print(dp[k])
