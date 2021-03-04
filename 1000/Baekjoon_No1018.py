n, m = map(int, input().split())
data = []
result = []

for _ in range(n):
    data.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        white_start = 0
        black_start = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if data[k][l] != 'W':
                        white_start += 1
                    if data[k][l] != 'B':
                        black_start += 1
                else:
                    if data[k][l] != 'B':
                        white_start += 1
                    if data[k][l] != 'W':
                        black_start += 1
        result.append(white_start)
        result.append(black_start)

print(min(result))
