n = int(input())
a = list(map(int, input().split()))
m = int(input())
s, e = 0, max(a)

while s <= e:
    mid = (s + e) // 2
    res = 0
    for i in a:
        if i > mid:
            res += mid
        else:
            res += i
    if res <= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)
