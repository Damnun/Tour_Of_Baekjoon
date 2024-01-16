n, m = map(int, input().split())
result = 1e9
x = []
y = []

for _ in range(m):
    pac, sin = map(int, input().split())
    x.append(pac)
    y.append(sin)

x.sort()
y.sort()

pac = x[0]
sin = y[0]

if n % 6 == 0:
    result = min(pac * (n // 6), sin * n, result)

else:
    result = min(pac * ((n // 6) + 1), sin * n, result, (pac * (n // 6) + sin * (n % 6)))

print(result)
