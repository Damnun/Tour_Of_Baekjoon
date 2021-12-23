import sys
from collections import deque

def bfs(a, b, graph, N):
    queue = deque()
    queue.append(a - 1)
    check = [-1] * N
    check[a - 1] = 0
    while queue:
        node = queue.popleft()
        for i in range(N):
            if (i - node) % graph[node] == 0 and check[i] == -1:
                queue.append(i)
                check[i] = check[node] + 1
                if i == b - 1:
                    return check[i]
    return -1

input = sys.stdin.readline
n = int(input())
graph = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, graph, n))
