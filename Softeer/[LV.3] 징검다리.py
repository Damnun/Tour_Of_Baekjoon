import sys
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
dp = [1] * n
result = 0

for i in range(1, n):
    cur = 0
    for j in range(i):
        if stones[j] < stones[i]:
            cur = max(cur, dp[j])
    dp[i] = cur + 1
    
print(max(dp))
