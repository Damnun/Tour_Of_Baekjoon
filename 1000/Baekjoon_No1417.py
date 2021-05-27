import heapq

N = int(input())
first = int(input())
data = []

for _ in range(N - 1):
    n = int(input())
    heapq.heappush(data, -n)
result = 0
while data:
    n = -heapq.heappop(data)
    if first > n:
        break
    first += 1
    result += 1
    heapq.heappush(data, -(n - 1))
print(result)

"""
우선순위 큐 // 최대 힙을 이용한 문제
1순위로 만들어야 하는 첫번째 값을 first라는 변수에 따로 저장해 둔 후
최대 힙에 나머지 변수들을 저장한다.
최대 힙에 있는 변수를 하나 꺼낸 후 first보다 크다면
first와 count를 1씩 증가시킨 후 변수는 -1을 하여 다시 힙에 집어넣는다.
이렇게 first가 최대 힙의 n보다 큰 경우가 루프의 종료 시점이 된다.
"""