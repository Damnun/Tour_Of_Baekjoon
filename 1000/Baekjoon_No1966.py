from collections import deque
import sys
loop = int(sys.stdin.readline())
for _ in range(loop):
    doc_count, index = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    queue = deque([(i, priority[i])for i in range(doc_count)])

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