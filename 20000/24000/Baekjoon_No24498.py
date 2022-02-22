import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = max(a)

for i in range(1, n - 1):
    if min((a[i - 1], a[i + 1])) > 0:
        ans = max((ans, a[i] + min((a[i - 1], a[i + 1]))))
print(ans)
