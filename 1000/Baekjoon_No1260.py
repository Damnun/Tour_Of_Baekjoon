from collections import deque


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()  # 스택의 제일 위 노드를 n에 저장
        if n not in visited:
            visited.append(n)  # 방문 처리
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]  # edge_info를 공백으로 분리하여 n1, n2에 넣어줌

    # n1 -> n2로 연결하는 graph
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    # n2 -> n1으로 연결하는 graph
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))
