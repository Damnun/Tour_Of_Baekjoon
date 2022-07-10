ans = 0
n = 0

for _ in range(10):
    a, b = map(int, input().split())
    n -= a
    n += b
    ans = max(ans, n)
print(ans)
