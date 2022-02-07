import heapq
data = []
n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))

    if not data:
        for i in a:
            heapq.heappush(data, i)
    else:
        for i in a:
            if data[0] < i:
                heapq.heappush(data, i)
                heapq.heappop(data)
print(data[0])
