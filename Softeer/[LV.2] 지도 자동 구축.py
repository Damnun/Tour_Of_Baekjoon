dp = [2, 3, 5]
n = int(input())

if n < 3:
    print(dp[n] ** 2)
    exit()

for i in range(2, n):
    dp.append(dp[i] * 2 - 1)

print(dp[n] ** 2)
