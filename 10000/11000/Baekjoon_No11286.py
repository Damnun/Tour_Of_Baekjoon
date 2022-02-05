import sys
import heapq
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        continue
    heapq.heappush(heap, (abs(x), x))
