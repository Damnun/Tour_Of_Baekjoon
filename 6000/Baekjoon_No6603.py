from itertools import combinations
import sys
input = sys.stdin.readline
data = list(map(int, input().split()))
ans = []
while data[0] != 0:
    su = data[1:]
    for i in combinations(su, 6):
        print(*(list(i)))
    print()
    data = list(map(int, input().split()))
