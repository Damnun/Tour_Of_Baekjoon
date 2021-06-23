n, m = map(int, input().split())
maps = [input() for _ in range(n)]
count = 0

for i in range(n):
    j = 0
    while j < m:
        if maps[i][j] == '|':
            j += 1
        else:
            count += 1
            while j < m and maps[i][j] == '-':
                j += 1

for j in range(m):
    i = 0
    while i < n:
        if maps[i][j] == '-':
            i += 1
        else:
            count += 1
            while i < n and maps[i][j] == '|':
                i += 1
print(count)
