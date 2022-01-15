n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = a[0][0]

for i in range(1, n):
    for j in range(0, i + 1):
        d[i][j] = max(d[i - 1][j] + a[i][j], d[i - 1][j - 1] + a[i][j])
print(max(d[n - 1]))

"""
i번 행의 j번째 수 (i, j)
지금 어디에 있는지에 따라 어디에 갈 수 있는지 <->
지금 어디에 있는지에 따라 어디서 왔는지
d[i][j] = (i, j)에 도착했을 때 합의 최대값
하 왼쪽 대각선 = (i + 1, j)
하 오른 대각선 = (i + 1, j + 1)
상 왼쪽 대각선 = (i - 1, j - 1)
상 오른 대각선 = (i - 1, j)

d[i][j] = max(d[i-1][j], d[i-1][j-1]) + a[i][j]

"""
