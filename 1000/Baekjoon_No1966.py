from collections import deque

loop = int(input())
for _ in range(loop):
    queue = deque()
    data = deque()
    doc_count, index = map(int, input().split())
    priority = list(map(int, input().split()))
    result = []
    for i in range(doc_count):
        queue.append((i, priority[i]))

    idx = 0
    while idx < doc_count:
        if queue[idx][1] == max(priority):
            priority.remove(queue[idx][1])
            idx += 1
        else:
            queue.append(queue[idx])
            queue.remove(queue[idx])

    for i in range(doc_count):
        if queue[i][0] == index:
            print(i + 1)
            break

"""
나름대로 만들어본 우선순위 큐
리팩토링이 절실해보인다
풀이시간 1시간

3
1 0 // 1

5
4 2
1 2 3 4 // 2

6 0
1 1 9 1 1 1 // 5
"""