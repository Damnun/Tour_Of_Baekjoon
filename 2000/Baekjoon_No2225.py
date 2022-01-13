MOD = 1000000000
n, k = map(int, input().split())
d = [[0] * (n + 1) for _ in range(k + 1)]
d[0][0] = 1
for i in range(1, k + 1):
    for j in range(0, n + 1):
        for l in range(0, j + 1):
            d[i][j] += d[i - 1][j - l]
        d[i][j] %= MOD
print(d[k][n])

"""
x + x + x + ... + L = N
일 때, L 이전까지의 수열들
합 = N - L개
개수 = K - 1개
이므로, D[K][N] = D[K - 1][N - L]이 된다.
"""
