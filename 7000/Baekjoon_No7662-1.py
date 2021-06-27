import heapq
import sys

T = int(sys.stdin.readline())  # 테스트 케이스
for _ in range(T):
    min_heap, max_heap = [], []
    visited = [False] * 1000001
    k = int(sys.stdin.readline())  # 연산의 개수

    for key in range(k):
        op, data = sys.stdin.readline().split()
        data = int(data)

        if op == 'I':
            heapq.heappush(min_heap, (data, key))
            heapq.heappush(max_heap, (data * -1, key))
            visited[key] = True

        elif op == 'D':
            if data == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

            elif data == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print("EMPTY")

"""
heap을 이용해 이중 우선순위 큐를 구현하였다.
파이썬에서는 최소힙 만을 지원하기에 기준 데이터에 -를 붙여서
꺼내 쓸 때 다시 양수로 만들어 최대 힙을 구현할 수 있었다.
최대 힙과 최소 힙으로 두가지를 나누어 매 순간마다 연산을 해주려고 하니
최대 힙과 최소 힙을 동기화 하는것과, 시간 초과라는 장벽이 찾아왔다
이를 visited 라는 배열과 key 값을 사용하여 서로간의 동기화를 시켜주어
시간 차이를 해결하였다.
"""
