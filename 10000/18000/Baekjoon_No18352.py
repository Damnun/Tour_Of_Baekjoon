from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도시 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시에서 출발 도시까지 거리는 0

# 모든 도로 정보 입력
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# BFS 실행
queue = deque([x])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 K인 도시의 번호 오름차순 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 최단 거리가 K인 도시가 없을 때 -1 출력
if check == False:
    print(-1)
