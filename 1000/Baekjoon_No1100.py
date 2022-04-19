MAX = 8
a = []
ans = 0
for _ in range(8):
    a.append(list(map(str, list(input()))))

for i in range(MAX):
    for j in range(MAX):
        if (i + j) % 2 == 0:
            if a[i][j] == 'F':
                ans += 1
print(ans)
