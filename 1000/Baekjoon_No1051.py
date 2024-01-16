n, m = map(int, input().split())
maps = []
result = 1

for _ in range(n):
    maps.append(input())

for i in range(min(n, m) + 1):
    for j in range(n - i):
        for k in range(m - i):
            current = maps[j][k]
            if current == maps[j][k + i] == maps[j + i][k] == maps[j + i][k + i]:
                result = (i + 1) ** 2
print(result)
