from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    for data in combinations(a, i):
        if sum(data) == s:
            count += 1
print(count)
"""
만약 연속하는 부분수열의 합이 S가 될 때 카운트를 구하는 문제였다면
itertools를 사용하는게 아닌 연속 수열을 구하는 재귀함수 (백트래킹)을 사용했어야 할 텐데
그게 아닌 단순 부분 수열이므로(무작위 무중복 무순서 추첨) combinations를 사용해 문제를 해결하였다.
"""
