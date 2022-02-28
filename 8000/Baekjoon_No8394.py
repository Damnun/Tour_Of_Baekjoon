n = m = 1
for _ in range(int(input())):
    n, m = m, (n + m) % 10
print(n)
