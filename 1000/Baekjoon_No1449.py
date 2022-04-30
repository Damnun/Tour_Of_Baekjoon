n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
s = a[0]
e = a[0] + l
ans = 1

for i in range(n):
    if s <= a[i] < e:
        continue
    else:
        s = a[i]
        e = a[i] + l
        ans += 1
print(ans)
