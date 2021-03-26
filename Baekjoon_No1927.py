import heapq
from sys import stdin
heap = []

for _ in range(int(stdin.readline())):
    tmp = int(stdin.readline())

    if tmp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print("0")

    else:
        heapq.heappush(heap, tmp)
