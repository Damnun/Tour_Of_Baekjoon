n = int(input())
if n < 2:
    print(n)
    exit()

dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n % (15 * (10 ** 5))):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[i])

https://getchan.github.io/algorithm/acmicpc_2749/
    