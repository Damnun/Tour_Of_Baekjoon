import sys
N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
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
DP 메모이제이션을 이용해 시간 초과 해결
11659번과 마찬가지의 해법으로 풀이하였따.
"""