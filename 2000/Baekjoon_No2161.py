n = int(input())
a = list(range(1, n + 1))
ans = []

while a:
    x = a.pop(0)
    ans.append(x)
    if a:
        x = a.pop(0)
        a.append(x)
print(*ans)
