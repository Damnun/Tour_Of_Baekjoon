import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

check = []
for i in permutations(data, m):
    check.append(i)
check = sorted(list(set(check)))
for i in check:
    print(*i)

"""
itertools의 permutations를 사용해 모든 경우의 수를 check에 저장.
중복 값을 제거하기 위해 set() 함수를 사용하나 한번에 정렬하기 위해
sorted에 넣어 사용하였음.

"""
