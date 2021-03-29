import sys
sys = sys.stdin.readline
from collections import deque


def bfs(s):
    count = 0
    queue = deque()
    queue.append(s)
    visit = [0] * (n + 1)
    visit[s] = 1
    while queue:
        here = queue.popleft()
        count += 1
        for w in relation[here]:
            if not visit[w]:
                visit[w] = 1
                queue.append(w)
    return count


n, m = map(int, input().split())
relation = [[] for _ in range(n + 1)]

for _ in range(m):
    one, two = map(int, input().split())
    relation[two].append(one)

max_count = 0
result = []

for i in range(1, n + 1):
    if relation[i]:
        tmp = bfs(i)
        if max_count <= tmp:
            if max_count < tmp:
                result = []
            max_count = tmp
            result.append(i)
print(*result)

"""
최적의 해킹 루트 찾기
BFS를 이용해 신뢰 관계가 제일 많은 pc를 찾아내어
순서대로 나열하는 문제인데, relation 설정을 1<->2가 아닌 1->2로 한다는 점이 특이했다.
BFS가 왜 이렇게 어렵게 느껴지는지 잘 모르곘다. 큰 벽을 만난 기분?
열심히 도전하고 열심히 깨지고 열심히 단단해져야겠다.
"""