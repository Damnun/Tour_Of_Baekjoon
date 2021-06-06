vertex_count, edge_count, vertex_number = map(int, input().split())
graph_list = [[] for _ in range(vertex_count + 1)]

# 정점간의 노드관계를 입력
for _ in range(edge_count):
    start, end = map(int, input().split())

    if graph_list[start].count(end) == 0:
        graph_list[start].append(end)
    if graph_list[end].count(start) == 0:
        graph_list[end].append(start)

# bfs(주위 값들을 리스트에 넣으며 진행)
def bfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            for i in sorted(graph[n]): # bfs이므로 오름차순으로 정렬된 값을 입력
                if i not in visited:
                    queue.append(i)
    return visited


def dfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop()
        if n not in visited:
            visited.append(n)
            queue.extend(sorted(graph[n], reverse=True)) # dfs 스택구조이므로 거꾸로 값을 넣어주어야함
    return visited


print(*dfs(graph_list, vertex_number))
print(*bfs(graph_list, vertex_number))

"""
BFS/DFS의 재공부
몇 번을 해도 이해되지 않는다는건 기초부터 잘못되었다는 뜻일테다.
BFS와 DFS를 이론을 기억해 최대한 스스로 구현해보았다. 
BFS와 DFS에서 스택 구조와 큐 구조에 따른 데이터의 정렬 방식의 차이를 이해하는게 시간이 조금 걸렸던 것 같다.

1차 32144, 736
2차 127040, 244
"""