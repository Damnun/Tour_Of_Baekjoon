import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
count = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited)
print(count)

"""
DFS, BFS는 정말 하루라도 복습하지 않는다면
이해도가 바닥으로 내리꽂는 알고리즘 인 것같다.
연결되어있는 요소를 덩어리 라고 생각하고, visited를 적극 활용하여
덩어리들을 한번에 1카운트로 셈해주고, 또 다음 반복에서 같은 덩어리가
나온다면 스킵해주는 방식으로 문제를 해결하였다.
"""