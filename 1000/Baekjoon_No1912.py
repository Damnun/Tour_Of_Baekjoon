"""
10
10 -4 3 1 5 6 -35 12 21 -1
"""
loop = int(input())
data = list(map(int, input().split()))
ans = [0 for _ in range(loop)]
result = -1001

for i in range(loop):
    ans[i] = max(ans[i-1] + data[i], data[i])
    result = max(result, ans[i])
print(result)