k, n, m = map(int, input().split())
result = (n*k) - m
if result <= 0:
    print("0")
else:
    print((n*k) - m)
