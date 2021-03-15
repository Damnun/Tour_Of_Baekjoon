import sys
from collections import deque
input = sys.stdin.readline

count = 0
com = int(input())
edge_count = int(input())
graph = [[] for i in range(com + 1)]
visit = [-1 for i in range(com + 1)]
queue = deque()

for _ in range(edge_count):
    x, y = map(int, input().split())
    if y not in graph[x]:
        graph[x].append(y)
    if x not in graph[y]:
        graph[y].append(x)

queue.append(1)
while queue:
    temp = queue.popleft()
    for i in graph[temp]:
        if visit[i] == -1:
            visit[i] = 1
            count += 1
            queue.append(i)
print(count - 1)

"""
BFS를 배우기 전에 대략적으로 구상을 통해 풀어보았다
사실 그래프 사이를 오가는 경로 탐색의 일종이라는데 생각보다 첫 삽을 뜨기가 어려웠다.
어떤 문제에 어떻게 적용해야하는지 알기까지는 많은 공부가 필요할 것 같다

"""