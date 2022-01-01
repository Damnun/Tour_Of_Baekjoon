# 1부터 n까지 자연수 중 중복 없이 m개를 고른 수열 전체
# 1 <= m < n <= 8
import sys
n, m = map(int, input().split())
data = [0] * m
c = [False] * (n + 1)

def go(index, n, m):
    if index == m:
        if sorted(data) == data:
            print(*data)
        return

    for i in range(1, n + 1):
        if c[i]:
            continue
        c[i] = True
        data[index] = i
        go(index + 1, n, m)
        c[i] = False

go(0, n, m)
