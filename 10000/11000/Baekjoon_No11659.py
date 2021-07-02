import sys
N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
dp = [data[0]]

for i in range(1, N):
    dp.append(dp[i-1] + data[i])

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(dp[end - 1])
    else:
        print(dp[end - 1] - dp[start - 2])

"""
DP를 이용해 시간초과 해결
미리 data 값을 dp에 메모이제이션 한 후
start 값에 따라 미리 구해둔 값을 빼주기만 하였다.
"""