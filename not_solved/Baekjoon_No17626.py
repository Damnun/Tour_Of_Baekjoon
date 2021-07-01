n = int(input())
dp = [0 for _ in range(n + 1)]

if n < 4:
    print(n)
    exit()

dp[1] = 1
dp[4] = 1

for i in range(5, n + 1):
    dp[i] = dp[i - 1] + dp[1]

print(dp)
print(dp[n])