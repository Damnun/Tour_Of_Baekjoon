"""
1. 사이클 찾기 DFS
2. 사이클 까지의 거리 찾기
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
from collections import deque

n = int(input())
a = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(n):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

check = [0] * (n + 1)  # 0: 미방문, 1: 방문, 2: 사이클
dist = [0] * (n + 1)


def dfs(x, count):
    if check[x]:
        if count - dist[x] >= 3:
            return x
        else:
            return -1
    check[x] = 1
    dist[x] = count
    for y in a[x]:
        tmp = dfs(y, count + 1)
        if tmp != -1:
            check[x] = 2
            if x == tmp:
                return -1
            else:
                return tmp
    return -1


dfs(1, 0)
queue = deque()
for i in range(1, n + 1):
    if check[i] == 2:
        dist[i] = 0
        queue.append(i)
    else:
        dist[i] = -1

while queue:
    x = queue.popleft()
    for y in a[x]:
        if dist[y] == -1:
            queue.append(y)
            dist[y] = dist[x] + 1

print(' '.join(map(str, dist[1:])))
