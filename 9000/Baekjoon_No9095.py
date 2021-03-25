loop = int(input())
dp = [1, 2, 4]

for i in range(3, 10):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
for i in range(loop):
    data = int(input())
    print(dp[data - 1])

"""
항 간의 관계 파악에 힘써보자
f(n) = f(n-1) + f(n-2) + f(n-3) (n > 3)
"""