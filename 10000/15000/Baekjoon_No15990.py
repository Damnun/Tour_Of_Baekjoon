"""
dp에서 조건으로 인해 점화식에 제약이 생긴다면 조건을 점화식에 넣어버려라.
d[i][j] = i를 1,2,3의 합으로 나타내는 방법의 수
j = 마지막에 사용한 수
"""
MAX = 100000
MOD = 1000000009
d = [[0] * 4 for _ in range(MAX + 1)]

for i in range(1, MAX + 1):
    if i - 1 >= 0:
        d[i][1] = d[i - 1][2] + d[i - 1][3]
        if i == 1:
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i - 2][1] + d[i - 2][3]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i - 3][1] + d[i - 3][2]
        if i == 3:
            d[i][3] = 1
    d[i][1] %= MOD
    d[i][2] %= MOD
    d[i][3] %= MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % MOD)
