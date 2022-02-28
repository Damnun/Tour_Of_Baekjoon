n, s, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
d = [[False] * (m + 1) for _ in range(n + 1)]
d[0][s] = True
for i in range(n):
    for j in range(m + 1):
        # 해당되는 칸인지 확인
        if not d[i][j]:
            continue

        # 범위 확인
        if j - a[i + 1] >= 0:
            d[i + 1][j - a[i + 1]] = True
        if j + a[i + 1] <= m:
            d[i + 1][j + a[i + 1]] = True

ans = -1
for i in range(m + 1):
    if d[n][i]:
        ans = i
print(ans)
