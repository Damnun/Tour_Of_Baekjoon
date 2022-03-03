n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [-1] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(k + 1):
        if j - coins[i] >= 0 and dp[j - coins[i]] != -1:
            if dp[j] == -1 or dp[j] > dp[j - coins[i]] + 1:
                dp[j] = dp[j - coins[i]] + 1
print(dp[k])
