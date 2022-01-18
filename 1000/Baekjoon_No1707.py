"""
한 그래프를 A,B로 나눌 수 있을 때 이분 그래프가 됨.
A에 포함되어 있는 정점끼리 연결된 간선 없음
B에 포함되어 있는 정점끼리 연결된 간선 없음
모든 간선의 한 끝 점은 A에, 다른 끝 점은 B에
시험문제중에 선 그어서 맞추는 문제랑 비슷하다고 보면 됨
A   1
B   2
C   3
"""
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    check[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        data = queue.popleft()
        for i in a[data]:
            if check[i] == 0:
                check[i] = -check[data]
                queue.append(i)
            else:
                if check[i] == check[data]:
                    return False
    return True

for i in range(int(input())):
    v, e = map(int, input().split())
    ans = True
    a = [[] for i in range(v + 1)]
    check = [0 for i in range(v + 1)]
    for j in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    for y in range(1, v + 1):
        if check[y] == 0:
            if not bfs(y):
                ans = False
                break
    print("YES" if ans else "NO")
