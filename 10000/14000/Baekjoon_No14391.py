"""
- 가로 조각과 세로 조각 두가지로 나뉨
- o과 1로 나누어진 NM개의 칸으로 생각 (max 16개)
- 4X4 공간을 1차원으로 이어붙여 생각 (max 16칸, 16자리 비트로 표현)

1. 비트마스크를 이용해 모든 경우를 구하고
2. 수의 합을 구해주면 된다

-A[I][J] -> i*m+j (row major order)
"""
n, m = map(int, input().rstrip().split())
a = [list(map(int, input())) for _ in range(n)]
ans = 0
for s in range(1 << (n * m)): # n * m 사이즈의 비트마스크
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i * m + j # row major order
            if (s & (1 << k)) == 0: # 가로일 경우
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i * m + j
            if (s & (1 << k)) != 0: # 세로일 경우
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)
