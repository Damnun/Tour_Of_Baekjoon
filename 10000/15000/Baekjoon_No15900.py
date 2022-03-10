n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [[1, 0]]
check[1] = -1
ls = []

while stack:
    cur, l = stack.pop()
    check[cur] = 1

    if cur != 1 and len(graph[cur]) == 1:
        ls.append(l)
        continue

    for next in graph[cur]:
        if check[next] == 0:
            stack.append([next, l + 1])

ls = sum(ls)
ans = "Yes" if ls % 2 else "No"
print(ans)



"""
1번 정점 = 루트 노드
자식이 없는 노드 = 리프 노드
1번 ~ n번 까지 순차적으로 부모-자식 관계 성립

- 모든 리프 노드에 토큰이 하나씩 있는 채로 시작
- 본인 턴에 토큰 중 하나를 부모 노드로 옮김
- 한 노드에 여러 토큰 상관 x
- 토큰이 루트 노드에 도착하면 토큰을 제거
- 본인 차례에 토큰이 모두 제거되면 패배

성원과 형석
성원이 먼저 시작, 형석이 나중 시작


"""
