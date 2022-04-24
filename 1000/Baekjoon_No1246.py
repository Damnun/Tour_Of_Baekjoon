import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = b = 0 
a = sorted([int(input()) for _ in range(m)])

for i in range(m):
    t = a[i] * ((m - i) if m - i <= n else n)
    if b < t:
        b = t
        p = a[i]
print(p, b)
