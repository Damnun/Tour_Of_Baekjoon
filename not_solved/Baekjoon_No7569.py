import sys
from collections import deque
input = sys.stdin.readline

result = 0
m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)

def dfs(x, y, z):
    global result, graph
    if x <= -1 or x > m or y <= -1 or y > n or z <= -1 or z > h:
        return False
    if graph[x][y][z] == 0:
        graph[x][y][z] = 1
        result += 1
        dfs(x + 1, y, z)
        dfs(x - 1, y, z)
        dfs(x, y + 1, z)
        dfs(x, y - 1, z)
        dfs(x, y, z + 1)
        dfs(x, y, z - 1)
        return True
    return False

for i in range(h):
    for j in range(n):
        for k in range(m):
            dfs(i, j, k)
print(result)
"""
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
"""