import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int ,input().split()))
queue = [i for i in range(1, n + 1)]

ans = 0
for i in range(m):
    queue_len = len(queue)
    queue_index = queue.index(a[i])
    if queue_index < queue_len - queue_index:
        while True:
            if queue[0] == a[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                ans += 1
    else:
        while True:
            if queue[0] == a[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                ans += 1
print(ans)
