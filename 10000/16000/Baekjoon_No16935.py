"""
[구현] [시뮬레이션]
5,6번 go()에
함수를 사분면처럼 구역을 나누어 이동시키는 방법을 잘 기억해두자.
"""

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
data = list(map(int, input().split()))


def go(data):
    n = len(a)
    m = len(a[0])

    if data == 1:
        ans = []
        ans = a[::-1]
        return ans

    elif data == 2:
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            ans[i] = list(reversed(a[i]))
        return ans

    elif data == 3:
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = a[n - j - 1][i]
        return ans

    elif data == 4:
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = a[j][m - i - 1]
        return ans

    elif data == 5:
        ans = [[0] * m for _ in range(n)]
        for i in range(n // 2):
            for j in range(m // 2):
                ans[i][j + m // 2] = a[i][j]
                ans[i + n // 2][j + m // 2] = a[i][j + m // 2]
                ans[i + n // 2][j] = a[i + n // 2][j + m // 2]
                ans[i][j] = a[i + n // 2][j]
        return ans

    elif data == 6:
        ans = [[0] * m for _ in range(n)]
        for i in range(n // 2):
            for j in range(m // 2):
                ans[i + n // 2][j] = a[i][j]
                ans[i][j] = a[i][j + m // 2]
                ans[i][j + m // 2] = a[i + n // 2][j + m // 2]
                ans[i + n // 2][j + m // 2] = a[i + n // 2][j]
        return ans


def print_a():
    for i in a:
        print(*i)
    return

for now in data:
    a = go(now)
print_a()
