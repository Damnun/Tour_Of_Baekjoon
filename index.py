vertex_count, edge_count, vertex_number = map(int, input().split())
graph_list = [[] for _ in range(vertex_count + 1)]

# 정점간의 노드관계를 입력
for _ in range(edge_count):
    start, end = map(int, input().split())

    if graph_list[start].count(end) == 0:
        graph_list[start].append(end)
    if graph_list[end].count(start) == 0:
        graph_list[end].append(start)

"""
# graph_list를 오름차순으로 정렬
for i in range(edge_count):
    graph_list[i].sort()
"""

# bfs(주위 값들을 리스트에 넣으며 진행)
def bfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            for i in sorted(graph[n]):
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
            queue.extend(sorted(graph[n], reverse=True))
    return visited


print(*dfs(graph_list, vertex_number))
print(bfs(graph_list, vertex_number))
