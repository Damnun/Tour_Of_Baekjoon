import sys
from collections import deque
input = sys.stdin.readline

count = 0
com = int(input())
edge_count = int(input())
graph = [[] for i in range(com + 1)]
visit = [-1 for i in range(com + 1)]
queue = deque()
queue.append(1)

for _ in range(edge_count):
    x, y = map(int, input().split())

    if y not in graph[x]:
        graph[x].append(y)
    if x not in graph[y]:
        graph[y].append(x)

def dfs(idx):
    global count, graph, visit
    for i in graph[idx]:
        if visit[i] == -1:
            visit[i] = 1
            count += 1
            dfs(i)
            
dfs(1)
print(count - 1)

"""
DFS를 사용하여 풀어본 바이러스 문제
1번 컴퓨터에서 네트워크(간선)으로 이어진 가장 깊은 루트를 탐색하여
몇 개의 노드를 방문했는지 파악하여 풀었음
이전에 사용했던 BFS보다 더 큰 메모리와 시간을 사용하였음
BFS와 DFS의 사용을 정확히 익히고 적시에 사용하는 법을 알아야겠다.
"""