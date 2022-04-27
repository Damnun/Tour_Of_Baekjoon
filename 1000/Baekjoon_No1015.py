n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
c = []

for i in range(n):
    now = b.index(a[i])
    c.append(now)
    b[now] = -1
print(*c)
