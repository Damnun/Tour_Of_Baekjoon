import heapq
import sys

left, right = [], []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max_heap
        heapq.heappush(left, (-num, num))
    else:
        # min_heap
        heapq.heappush(right, (num, num))

    # 오른쪽 값에 원소가 있으면서
    # 왼쪽 값이 오른쪽 값보다 큰 경우
    # left 원소보다 right 원소가 더 커야하는 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    print(left[0][1])

"""
최소/최대 Heap을 사용하여 중간값을 찾아내는 문제이다.

처음에는 리스트에 값을 입력받을 때마다 정렬을 해준 후 중간 값을 출력하려고 했으나, 시간 초과가 나왔다.

입력 개수가 10만개가 넘어가는데 이를  매 루프마다 정렬해주게 된다면 n2 * log n 꼴로 비약적으로 수가 늘어나게 되어 당연히 시간초과가 나게 된다.

루트 노드에 최소/최대가 오는 힙 정렬을 이용하여 중간값을 기준으로 왼쪽 값들의 최대값 / 오른쪽 값들의 최소값을 비교하여 중간값을 유지하는 방법을 선택할 수 있었다.

우선순위 큐와 힙정렬에 대하여 더욱 열심히 공부해 보아야 겠다.

관련문제 : No.5397
"""