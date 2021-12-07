import heapq
n = int(input())
data = list(int(input()) for _ in range(n))
heapq.heapify(data) # heapify를 통해 기존 리스트를 heap으로 변환
result = 0

while len(data) != 1:
    num1 = heapq.heappop(data)
    num2 = heapq.heappop(data)
    result += num1 + num2
    heapq.heappush(data, num1 + num2)
print(result)
