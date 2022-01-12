"""
N개의 카드 구매
N개의 카드 종류
I번째 카드팩은 I개의 카드, 가격은 P[I]원
카드 N개 구매의 최대비용 구하기
"""

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + p[j])
print(d[n])
