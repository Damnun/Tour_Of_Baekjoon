n, l = map(int, input().split())

for i in range(l, 101):
    x = n / i - (i + 1) / 2
    if int(x) == x:
        x = int(x)
        if x + 1 >= 0:
            for j in range(x + 1, x + i + 1):
                print(j, end=" ")
            break
else:
    print(-1)
