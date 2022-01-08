from itertools import permutations
n = int(input())
data = list(map(int, input().split()))
ans = 0

for a in permutations(data, n):
    tmp = 0
    for i in range(1, len(a)):
        tmp += abs(a[i] - a[i - 1])
    ans = max(tmp, ans)
print(ans)
