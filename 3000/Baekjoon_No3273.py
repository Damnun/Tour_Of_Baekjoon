n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()

ans = 0
l, r = 0, n - 1
while l < r:
    cur = a[l] + a[r]
    if cur == x:
        ans += 1
        l += 1
    elif cur < x:
        l += 1
    else:
        r -= 1
print(ans)
