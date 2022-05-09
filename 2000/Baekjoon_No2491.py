n = int(input())
a = list(map(int, input().split()))
dp, dp2 = [1] * n, [1] * n
for i in range(1, n):
    if a[i] <= a[i - 1]:
        dp[i] = max(dp[i], dp[i - 1] + 1)
    if a[i] >= a[i - 1]:
        dp2[i] = max(dp2[i], dp2[i - 1] + 1)
print(max(max(dp), max(dp2)))
