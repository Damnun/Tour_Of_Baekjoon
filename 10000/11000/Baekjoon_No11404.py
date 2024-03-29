n = int(input())
m = int(input())
s = [[100000000] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    if s[a - 1][b - 1] > c:
        s[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for i in s:
    for j in i:
        if j == 100000000:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
