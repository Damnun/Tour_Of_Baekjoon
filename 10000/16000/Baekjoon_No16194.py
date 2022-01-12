"""
N개의 카드 구매
N개의 카드 종류
I번째 카드팩은 I개의 카드, 가격은 P[I]원
카드 N개 구매의 최소비용 구하기
min 함수를 사용하니 d의 초기화를 매우 큰 값(연산에서 나올 수 없을 정도로)
으로 정해주어야 한다.
"""

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] + [1000 * 10000] * n

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = min(d[i], d[i - j] + p[j])
print(d[n])
