data = int(input())
dp = [0 for _ in range(data + 1)]

if data == 0:
    print("0")
    quit()

dp[0] = 0
dp[1] = 1

for i in range(2, data + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[data])
