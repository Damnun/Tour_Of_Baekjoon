data = int(input())
if data == 1:
    print("4")
    quit()

dp = [0 for _ in range(data + 1)]
result = 0
dp[0] = 1
dp[1] = 1

for i in range(2, data + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    result = (dp[i - 1] * 4) + (dp[i - 2] * 2)
print(result)
