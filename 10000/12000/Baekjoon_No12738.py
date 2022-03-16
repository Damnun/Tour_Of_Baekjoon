import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

queue = []  # LIS
temp = []  # LIS 값의 인덱스, 값
for i in a:
    if not queue or i > queue[-1]:
        queue.append(i)
        temp.append((len(queue) - 1, i))
    else:
        queue[bisect_left(queue, i)] = i
        temp.append((bisect_left(queue, i), i))
ans = []
idx = len(queue) - 1
for i in range(len(temp) - 1, -1, -1):
    if temp[i][0] == idx:
        ans.append(temp[i][1])
        idx -= 1
print(len(ans))
print(*reversed(ans))
