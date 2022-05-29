p = 0
ans = 0
a, b, c, m = map(int, input().split())

for i in range(24):
    if p + a <= m:
        p += a
        ans += b
    else:
        if p - c >= 0:
            p -= c
        else:
            p = 0
print(ans)
