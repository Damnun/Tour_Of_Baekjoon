# BFS + 소수 판별
from collections import deque
def change(num, index, digit):
    if index == 0 and digit == 0:
        return -1
    s = list(str(num))
    s[index] = chr(digit + ord('0'))
    return int(''.join(s))


prime = [False] * 10001
for i in range(2, 10001):
    if not prime[i]:
        for j in range(i * i, 10001, i):
            prime[j] = True
for i in range(10001):
    prime[i] = not prime[i]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c = [False] * 10001
    d = [0] * 10001
    d[n] = 0
    c[n] = True
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()
        for i in range(4):
            for j in range(10):
                next = change(now, i, j)
                if next != -1:
                    if prime[next] and not c[next]:
                        queue.append(next)
                        d[next] = d[now] + 1
                        c[next] = True
    print(d[m])
