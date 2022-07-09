n = int(input())
s, ans = 0, 0
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == 1:
        s += 1
        ans += s
    else:
        s = 0
print(ans)
